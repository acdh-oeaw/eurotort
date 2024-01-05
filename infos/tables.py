import django_tables2 as tables

from .models import AboutTheProject
from .models import ProjectInst
from .models import TeamMember


class AboutTheProjectTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")

    class Meta:
        model = AboutTheProject
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class TeamMemberTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")

    class Meta:
        model = TeamMember
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}


class ProjectInstTable(tables.Table):
    id = tables.LinkColumn(verbose_name="ID")

    class Meta:
        model = ProjectInst
        sequence = ("id",)
        attrs = {"class": "table table-responsive table-hover"}
