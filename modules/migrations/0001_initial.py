# Generated by Django 5.0.6 on 2024-06-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(
                    max_length=100,
                    verbose_name="Название"
                )),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        max_length=300,
                        null=True,
                        verbose_name="Описание"
                    ),
                ),
            ],
            options={
                "verbose_name": "Образовательный модуль",
                "verbose_name_plural": "Образовательные модули",
                "ordering": ("title",),
            },
        ),
    ]
