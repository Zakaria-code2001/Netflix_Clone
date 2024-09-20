from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Opzioni per le categorie di età
AGE_CHOICES = (
    ("All", "All"),
    ("Kids", "Kids"),
)

# Opzioni per i tipi di film
MOVIE_CHOICES = (
    ("seasonal", "Seasonal"),
    ("single", "Single"),
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField("Profile", blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=1000)
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="videos/")

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField(
        Video, related_name="movies"
    )  # Aggiunta del related_name
    image = models.ImageField(upload_to="covers")
    age_limit = models.CharField(choices=AGE_CHOICES, max_length=10)

    def __str__(self):
        return self.title
