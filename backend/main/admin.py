from django.contrib import admin
from .models import *


class ShowId(admin.ModelAdmin):
    readonly_fields = ['id']


admin.site.register(User, ShowId)
admin.site.register(Project, ShowId)
admin.site.register(CustomProjectRequest, ShowId)
admin.site.register(SelectProjectRequest, ShowId)