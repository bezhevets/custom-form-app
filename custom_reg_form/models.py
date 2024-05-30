from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class Category(models.Model):
    """
    This model represents a category with a tag name, active status, and timestamps.
    """
    name = models.CharField(max_length=100, verbose_name="Tag Name")

    def __str__(self):
        return self.name


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)

    favorite_movie = models.CharField(
        verbose_name="Fav Flick",
        max_length=100,
    )
    categories = models.ManyToManyField("Category", related_name="extra_info")


# from django.conf import settings
# from django.db import models
#
# # Backwards compatible settings.AUTH_USER_MODEL
# USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")
#
#
# class ExtraInfo(models.Model):
#     """
#     This model contains two extra fields that will be saved when a user registers.
#     The form that wraps this model is in the forms.py file.
#     """
#
#     user = models.OneToOneField(
#         USER_MODEL, null=True, related_name="user+", on_delete=models.CASCADE
#     )
#     categories = models.CharField(
#         verbose_name="Interests",
#         max_length=500,
#     )
#
#     def __str__(self):
#         result = "{0.user} {0.interests}"
#         return result.format(self)
