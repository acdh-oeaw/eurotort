# Generated by Django 5.0 on 2023-12-07 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "archiv",
            "0015_alter_court_is_high_court_alter_courtdecission_court_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="court",
            name="is_high_court",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="True if court is the highest court in a country in the relevant field",
                null=True,
                verbose_name="Highest Court",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="partial_legal_system",
            field=models.ForeignKey(
                blank=True,
                help_text="Legal system",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rvn_courtdecission_partial_legal_system_partiallegalsystem",
                to="archiv.partiallegalsystem",
                verbose_name="Legal system",
            ),
        ),
        migrations.AlterField(
            model_name="keyword",
            name="name",
            field=models.CharField(
                blank=True, help_text="Keyword", max_length=250, verbose_name="Keyword"
            ),
        ),
        migrations.AlterField(
            model_name="keyword",
            name="part_of",
            field=models.ForeignKey(
                blank=True,
                help_text="Parent Keyword",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rvn_keyword_part_of_keyword",
                to="archiv.keyword",
                verbose_name="Parent",
            ),
        ),
        migrations.AlterField(
            model_name="keyword",
            name="see_also",
            field=models.ManyToManyField(
                blank=True,
                help_text="Related keyword(s)",
                to="archiv.keyword",
                verbose_name="Related to",
            ),
        ),
        migrations.AlterField(
            model_name="yearbook",
            name="part_of",
            field=models.ForeignKey(
                blank=True,
                help_text="For chapters, select volume here",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="has_bibliographic_items",
                to="archiv.yearbook",
                verbose_name="Parent",
            ),
        ),
    ]
