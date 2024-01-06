from django.core.management.base import BaseCommand
from tqdm import tqdm

from archiv.models import YearBook


class Command(BaseCommand):
    help = "Creates parent bibliographic items"

    def handle(self, *args, **kwargs):
        for x in tqdm(
            YearBook.objects.filter(has_bibliographic_items=None).filter(part_of=None)
        ):
            if "Digest" in x.title:
                new_title = x.title.split(" in: ")[-1]
            elif "European Tort Law" in x.title:
                new_title = x.title.split("in: ")[-1]
            else:
                continue
            parent, _ = YearBook.objects.get_or_create(title=new_title)
            x.part_of = parent
            x.save()
        for x in YearBook.objects.all():
            x.save()
