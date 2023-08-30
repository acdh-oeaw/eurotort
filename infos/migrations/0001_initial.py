# Generated by Django 3.2.8 on 2021-10-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutTheProject",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Project's Title"
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Project's Sub Title"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Project Description"),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True,
                        help_text="The names of the Agents responsible for this description",
                        max_length=250,
                        verbose_name="Authors",
                    ),
                ),
                (
                    "github",
                    models.CharField(
                        blank=True,
                        help_text="Link to the application's source code",
                        max_length=250,
                        verbose_name="Code Repo",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "About the Project",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="ProjectInst",
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
                (
                    "name",
                    models.CharField(blank=True, max_length=300, verbose_name="Name"),
                ),
                (
                    "abbr",
                    models.CharField(
                        blank=True, max_length=300, verbose_name="Abbreviation"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, verbose_name="Short description of the Institution"
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True,
                        max_length=300,
                        verbose_name="Link to the Institution's website",
                    ),
                ),
                (
                    "logo_url",
                    models.URLField(
                        blank=True,
                        max_length=300,
                        verbose_name="Link to the Insitution's Logo",
                    ),
                ),
                (
                    "norm_url",
                    models.URLField(
                        blank=True,
                        help_text="URL to any normdata record of the institution",
                        max_length=300,
                        verbose_name="Norm Data URL (OCRID, GND, VIAF, ...)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Institution involved in the Project",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="TeamMember",
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
                (
                    "name",
                    models.CharField(blank=True, max_length=300, verbose_name="Name"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, verbose_name="Short description of the Person"
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True,
                        max_length=300,
                        verbose_name="Link to the person's website",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        help_text="will be used to group the team member",
                        max_length=300,
                        verbose_name="The person's role in the project",
                    ),
                ),
                (
                    "norm_url",
                    models.URLField(
                        blank=True,
                        help_text="URL to any normdata record of the person",
                        max_length=300,
                        verbose_name="Norm Data URL (OCRID, GND, VIAF, ...)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Team Member",
                "ordering": ["role", "name"],
            },
        ),
    ]
