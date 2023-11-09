# Generated by Django 4.2.4 on 2023-11-09 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("archiv", "0011_alter_tag_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="court",
            options={"ordering": ["name"], "verbose_name": "Deciding court"},
        ),
        migrations.AlterModelOptions(
            name="courtdecission",
            options={"ordering": ["id"], "verbose_name": "Case"},
        ),
        migrations.AddField(
            model_name="court",
            name="name_english",
            field=models.CharField(
                blank=True,
                help_text="Court name (translated into English)",
                max_length=250,
                verbose_name="Court name (translated)",
            ),
        ),
        migrations.AddField(
            model_name="court",
            name="note",
            field=models.TextField(
                blank=True, help_text="Optional notes", null=True, verbose_name="Notes"
            ),
        ),
        migrations.AddField(
            model_name="courtdecission",
            name="related_decision",
            field=models.ManyToManyField(
                blank=True,
                help_text="Related decisions",
                related_name="has_related_decisions",
                to="archiv.courtdecission",
                verbose_name="Related decisions",
            ),
        ),
        migrations.AddField(
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
        migrations.AlterField(
            model_name="court",
            name="is_high_court",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="True, if court is a highest court in a country",
                null=True,
                verbose_name="Highest Court",
            ),
        ),
        migrations.AlterField(
            model_name="court",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Court name (in original language)",
                max_length=250,
                verbose_name="Court",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="additional_information",
            field=models.TextField(
                blank=True,
                help_text="Additional information provided by the author (e.g. related publications, comments etc.)",
                null=True,
                verbose_name="Additional information",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="author",
            field=models.ManyToManyField(
                blank=True,
                help_text="Author",
                related_name="rvn_courtdecission_author_person",
                to="archiv.person",
                verbose_name="Author",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="commentary",
            field=models.TextField(
                blank=True,
                help_text="Commentary by the author",
                null=True,
                verbose_name="Commentary",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="file_number",
            field=models.CharField(
                blank=True,
                help_text="Case number (file number/reference as cited in the given legal system, e.g. '[2010] UKSC 33' for a UK Supreme Court decision or _VI ZR 548/12' for a German BGH decision)",
                max_length=250,
                verbose_name="Case number",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="location",
            field=models.TextField(
                blank=True,
                help_text="Reference to law report or journal reporting the case in a given legal system",
                null=True,
                verbose_name="Reported in",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="party",
            field=models.CharField(
                blank=True,
                help_text="Parties or name of the case (if cited in the given legal system)",
                max_length=250,
                verbose_name="Parties",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="short_description",
            field=models.TextField(
                blank=True,
                help_text="Brief information on what the case concerns (for Yearbook cases, this is the headline provided by the author)",
                null=True,
                verbose_name="Subject matter",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="situation",
            field=models.TextField(
                blank=True,
                help_text="Summary of the facts",
                null=True,
                verbose_name="Facts",
            ),
        ),
        migrations.AlterField(
            model_name="courtdecission",
            name="year_book_title",
            field=models.ForeignKey(
                blank=True,
                help_text="Bibliographic source",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="related_court_decission",
                to="archiv.yearbook",
                verbose_name="Bibliographic source",
            ),
        ),
        migrations.AlterField(
            model_name="partiallegalsystem",
            name="link_to_legal_db",
            field=models.URLField(
                blank=True,
                help_text="Link to legal db",
                null=True,
                verbose_name="Legal database",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="contact",
            field=models.EmailField(
                blank=True,
                help_text="E-mail address",
                max_length=254,
                verbose_name="Contact",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="first_name",
            field=models.CharField(
                blank=True,
                help_text="First name",
                max_length=250,
                verbose_name="First name",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="last_name",
            field=models.CharField(
                blank=True,
                help_text="Last name",
                max_length=250,
                verbose_name="Last name",
            ),
        ),
        migrations.AlterField(
            model_name="yearbook",
            name="title",
            field=models.CharField(
                blank=True,
                help_text="Bibliographic source",
                max_length=500,
                verbose_name="Bibliographic source",
            ),
        ),
    ]
