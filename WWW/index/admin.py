from django.contrib import admin
from .models import TeamMember, Ad, Client, FinishedProject

# Register your models here.
admin.site.register(TeamMember)
admin.site.register(Ad)
admin.site.register(Client)
admin.site.register(FinishedProject)