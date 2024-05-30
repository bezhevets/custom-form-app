from django.contrib import admin
from .models import ExtraInfo

admin.site.register(ExtraInfo)

# from django.contrib import admin
# from .models import ExtraInfo
#
#
# @admin.register(ExtraInfo)
# class ExtraInfoAdmin(admin.ModelAdmin):
#     list_display = ("user", "categories")
#     search_fields = ("user",)
#     fields = ("user",)
