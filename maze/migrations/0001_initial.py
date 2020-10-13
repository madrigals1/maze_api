# Generated by Django 3.1.2 on 2020-10-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Maze",
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
                ("width", models.IntegerField(default=20)),
                ("height", models.IntegerField(default=20)),
            ],
        ),
    ]
