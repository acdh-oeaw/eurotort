from django.contrib import admin

from infos.models import AboutTheProject
from infos.models import ProjectInst
from infos.models import TeamMember

admin.site.register(ProjectInst)
admin.site.register(TeamMember)
admin.site.register(AboutTheProject)
