# Generated by Django 3.1b1 on 2020-06-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photograph", "0001_implement_photograph_model"),
    ]

    operations = [
        migrations.AddField(
            model_name="photograph",
            name="audio",
            field=models.FileField(blank=True, null=True, upload_to="audio/"),
        ),
        migrations.AddField(
            model_name="photograph",
            name="audio_duration",
            field=models.FloatField(editable=False, null=True),
        ),
    ]
