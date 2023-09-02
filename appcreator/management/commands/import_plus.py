import pandas as pd
import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import CourtDecission, KeyWord, Person, YearBook


class Command(BaseCommand):
    help = "Import Data"

    def handle(self, *args, **kwargs):
        df = pd.read_csv("./data/tb_ENAUT.csv")
        print(f"adding {len(df)} Decission-Author relations")
        for i, row in tqdm(df.iterrows(), total=len(df)):
            try:
                court = CourtDecission.objects.get(legacy_pk=row["ENAUT_Entscheidung"])
                autor = Person.objects.filter(legacy_pk=row["ENAUT_Autor"])
            except ObjectDoesNotExist:
                continue
            court.author.add(*autor)

        df = pd.read_csv("./data/tb_ENST.csv")
        print(f"adding {len(df)} Decission-Keyword relations")
        for i, row in tqdm(df.iterrows(), total=len(df)):
            try:
                court = CourtDecission.objects.get(legacy_pk=row["ENST_Entscheidung"])
            except:
                print(row["ENST_Entscheidung"])
                continue
            kw = KeyWord.objects.filter(legacy_pk=row["ENST_Stichwort"])
            court.keyword.add(*kw)

        print(f"now adding Yearbooks")
        qs = CourtDecission.objects.all()
        for x in tqdm(qs, total=qs.count()):
            data = json.loads(x.orig_data_csv)["entscheidung_yearbook"]
            if isinstance(data, str):
                if ")" in data:
                    items = data.split(") ")
                    page = items[-1]
                    title = f'{" ".join(items[:-1])})'
                    yearbook, _ = YearBook.objects.get_or_create(title=title)
                    x.year_book_title = yearbook
                    x.year_book_issue = page[:249]
                    try:
                        x.save()
                    except:
                        print(x.id, yearbook, page)
