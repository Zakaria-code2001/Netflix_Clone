from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile, Movie
from django.contrib.auth import logout
from django.urls import reverse

class Home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("nflx_app:profile-list")
        return render(request, "nflx_app/index.html")


method_decorator(login_required, name="dispatch")


class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        context = {"profiles": profiles}
        return render(request, "nflx_app/profilelist.html", context)

    def post(self, request, *args, **kwargs):
        profile_id = request.POST.get('profile_id')
        if profile_id:
            profile = get_object_or_404(Profile, id=profile_id)
            if profile in request.user.profiles.all():
                request.user.profiles.remove(profile)
                profile.delete()
        return redirect('nflx_app:profile-list')


method_decorator(login_required, name="dispatch")


class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        form = ProfileForm()
        context = {"form": form}
        return render(request, "nflx_app/profilecreate.html", context)

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect("nflx_app:profile-list")
        context = {"form": form}
        return render(request, "nflx_app/profilecreate.html", context)


method_decorator(login_required, name="dispatch")


class MovieList(View):
    def get(self, request, profile_id, *args, **kwargs):
        try:
            profile = Profile.objects.get(uuid=profile_id)
            movies = Movie.objects.filter(age_limit=profile.age_limit)

            # Check if the profile is associated with the user
            if profile not in request.user.profiles.all():
                return redirect("nflx_app:profile-list")

            # Handle search functionality
            query = request.GET.get('query')
            if query:
                movies = movies.filter(title__icontains=query)  # Adjust 'title' to your model's search field

            context = {
                "movies": movies,
                "query": query  # Pass the query to the template for display
            }

            return render(request, "nflx_app/movielist.html", context)
        except Profile.DoesNotExist:
            return redirect("nflx_app:profile-list")


method_decorator(login_required, name="dispatch")


class MovieDetail(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)

            context = {"movie": movie}

            return render(request, "nflx_app/moviedetail.html", context)
        except Movie.DoesNotExist:
            return redirect("nflx_app:profile-list")


method_decorator(login_required, name="dispatch")


class PlayMovie(View):
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            movie = movie.video.values()

            context = {"movie": list(movie)}

            return render(request, "nflx_app/playmovie.html", context)
        except Movie.DoesNotExist:
            return redirect("nflx_app:profile-list")

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('nflx_app:Home'))