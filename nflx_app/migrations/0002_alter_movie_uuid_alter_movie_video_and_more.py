# Generated by Django 5.1.1 on 2024-09-20 09:29

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nflx_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name="movie",
            name="video",
            field=models.ManyToManyField(related_name="movies", to="nflx_app.video"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
