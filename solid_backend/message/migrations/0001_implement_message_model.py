# Generated by Django 3.0.3 on 2020-04-15 17:41

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("CL", "Changlog"),
                            ("SE", "Series"),
                            ("NO", "Notice"),
                        ],
                        max_length=2,
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "text",
                    models.TextField(
                        blank=True, default="", verbose_name="text (Markdown)"
                    ),
                ),
                ("img", models.ImageField(blank=True, null=True, upload_to="message/")),
                ("img_alt", models.CharField(blank=True, default="", max_length=200)),
                ("valid_from", models.DateField(default=datetime.date.today)),
                ("valid_to", models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
