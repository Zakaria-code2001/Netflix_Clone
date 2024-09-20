from django.contrib import admin
from nflx_app.models import Movie, Video, Profile, CustomUser


admin.site.register(Movie)
admin.site.register(Video)
admin.site.register(Profile)
admin.site.register(CustomUser)
