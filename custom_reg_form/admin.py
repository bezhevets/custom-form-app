from django.contrib import admin
from .models import ExtraInfo


class ExtraInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "interests",)
    list_display_links = ("user", "interests",)
    list_filter = ("user",)
    search_fields = ("user",)
    list_per_page = 25

admin.site.register(ExtraInfo, ExtraInfoAdmin)
