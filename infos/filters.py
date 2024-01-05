# generated by appcreator
import django_filters

from .models import AboutTheProject
from .models import ProjectInst
from .models import TeamMember


class TeamMemberListFilter(django_filters.FilterSet):
    class Meta:
        model = TeamMember
        fields = ["id", "name", "website", "role"]


class AboutTheProjectListFilter(django_filters.FilterSet):
    class Meta:
        model = AboutTheProject
        fields = ["id", "author"]


class ProjectInstListFilter(django_filters.FilterSet):
    class Meta:
        model = ProjectInst
        fields = ["id", "name", "website"]
