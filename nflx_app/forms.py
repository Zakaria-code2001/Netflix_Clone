from django.forms import ModelForm
from nflx_app.models import Profile
from django import forms


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ["uuid"]

