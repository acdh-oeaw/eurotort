# Generated by Django 5.0 on 2024-07-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("archiv", "0020_keyword_linked_to_cases_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courtdecission",
            name="tag",
            field=models.ManyToManyField(
                blank=True,
                help_text="Tags",
                related_name="has_related_tags",
                to="archiv.tag",
                verbose_name="Tags",
            ),
        ),
    ]