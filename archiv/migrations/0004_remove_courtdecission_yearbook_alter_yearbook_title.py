# Generated by Django 4.2.4 on 2023-09-02 09:27

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("archiv", "0003_courtdecission_year_book_issue_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="courtdecission",
            name="yearbook",
        ),
        migrations.AlterField(
            model_name="yearbook",
            name="title",
            field=models.CharField(
                blank=True, help_text="Title", max_length=500, verbose_name="Title"
            ),
        ),
    ]
