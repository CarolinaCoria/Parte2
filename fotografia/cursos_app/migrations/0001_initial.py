# Generated by Django 5.0 on 2023-12-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cursos",
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
                ("nombre", models.CharField(default="Alumno x", max_length=100)),
                ("duracion", models.CharField(default="Meses x", max_length=100)),
                (
                    "contacto",
                    models.EmailField(default="no_contact@mail.com", max_length=100),
                ),
                ("horario", models.CharField(default="Horario x", max_length=100)),
                ("fecha_comienzo", models.DateField(auto_now=True)),
            ],
            options={
                "db_table": "cursos_fotografia",
            },
        ),
    ]