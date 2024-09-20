from django.urls import path
from .views import Home, ProfileList, ProfileCreate, MovieList, MovieDetail, PlayMovie, LogoutView


app_name = "nflx_app"

urlpatterns = [
    path("", Home.as_view(), name="Home"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("profiles/", ProfileList.as_view(), name="profile-list"),
    path("profiles/create/", ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>/', MovieDetail.as_view(),
         name="movie-detail"),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name="play-movie"),
]
