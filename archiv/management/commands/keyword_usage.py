import os

import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import Count

from archiv.models import CourtDecission
from archiv.models import KeyWord


class Command(BaseCommand):
    help = "Create KeyWord Usage Statistic"

    def handle(self, *args, **kwargs):
        report_dir = os.path.join(settings.MEDIA_ROOT, "reports")
        os.makedirs(report_dir, exist_ok=True)

        print("reporting usage of keywords")
        keyword_stats = os.path.join(report_dir, "keyword-stats.html")
        data = list(
            KeyWord.objects.annotate(
                Count("rvn_courtdecission_keyword_keyword")
            ).values(
                "id",
                "part_of__name",
                "name",
                "rvn_courtdecission_keyword_keyword__count",
            )
        )
        df = (
            pd.DataFrame(data)
            .rename(columns={"rvn_courtdecission_keyword_keyword__count": "count"})
            .sort_values(by=["part_of__name", "count"])
        )
        df.to_html(keyword_stats, index=False)
        df.to_csv(keyword_stats.replace(".html", ".csv"), index=False)

        print("reporting of keyword-decission relation")
        keyword_stats = os.path.join(report_dir, "keyword-cases.html")
        data = (
            CourtDecission.objects.annotate(Count("keyword"))
            .values("id", "keyword__count")
            .distinct()
        )
        df = pd.DataFrame(list(data))
        new_data = df.groupby("keyword__count").size()
        ndf = (
            pd.DataFrame(new_data)
            .reset_index()
            .rename(columns={0: "court_decissions", "keyword__count": "keywords"})
        )
        ndf.to_html(keyword_stats, index=False)
        ndf.to_csv(keyword_stats.replace(".html", ".csv"), index=False)
