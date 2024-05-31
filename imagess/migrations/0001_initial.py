# Generated by Django 5.0.6 on 2024-05-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("image", models.ImageField(upload_to="images/")),
                ("size", models.IntegerField(blank=True, default=1024, null=True)),
                ("type", models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Resim",
                "verbose_name_plural": "Resimler",
            },
        ),
    ]
