from .models import ExtraInfo
from django.forms import ModelForm, CheckboxSelectMultiple


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['favorite_movie'].error_messages = {
            "required": u"Please tell us your favorite movie.",
            "invalid": u"We're pretty sure you made that movie up.",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('favorite_movie', 'categories')
        widgets = {
            'categories': CheckboxSelectMultiple(),
        }

# class ExtraInfoForm(ModelForm):
#     """
#     The fields on this form are derived from the ExtraInfo model in models.py.
#     """
#     def __init__(self, *args, **kwargs):
#         super(ExtraInfoForm, self).__init__(*args, **kwargs)
#         self.fields['favorite_movie'].error_messages = {
#             "required": u"Please tell us your favorite movie.",
#             "invalid": u"We're pretty sure you made that movie up.",
#         }
#         self.fields['favorite_editor'].error_messages = {
#             "required": u"Please select your favorite editor.",
#             "invalid": u"Invalid selection for favorite editor.",
#         }
#
#     class Meta(object):
#         model = ExtraInfo
#         fields = ('favorite_editor', 'favorite_movie')
#         labels = {
#             'favorite_movie': 'Favorite Movie',
#             'favorite_editor': 'Favorite Editor',
#         }

# import requests
# from requests.auth import HTTPBasicAuth
#
# from django import forms
# from django.forms import ModelForm
# from .models import ExtraInfo
#
# class ExtraInfoForm(ModelForm):
#     """
#     The fields on this form are derived from the ExtraInfo model in models.py.
#     """
#     def __init__(self, *args, **kwargs):
#         super(ExtraInfoForm, self).__init__(*args, **kwargs)
#         self.fields["categories"].required = True
#
#     class Meta(object):
#         model = ExtraInfo
#         fields = ("categories",)
#         labels = {"categories": "Categories"}
#         help_text = {"categories": "Сhoose your interests"}

# # Статичні варіанти для поля вибору
# CATEGORY_CHOICES = [
#     ('option1', 'Option 1'),
#     ('option2', 'Option 2'),
#     ('option3', 'Option 3'),
# ]
#
#
# class ExtraInfoForm(ModelForm):
#     categories = forms.MultipleChoiceField(
#         choices=CATEGORY_CHOICES,  # Тут можна буде змінити на динамічні варіанти
#         widget=forms.CheckboxSelectMultiple,
#         label="Select multiple options",
#         required=True,
#     )
#
#     class Meta:
#         model = ExtraInfo
#         fields = ("categories",)
#         labels = {"categories": "Categories"}
#         help_text = {'categories': "Choose your interests"}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['categories'].required = True
#         if self.instance and self.instance.categories:
#             self.initial['categories'] = self.instance.categories.split(',')
#
#     def clean_categories(self):
#         categories = self.cleaned_data.get('categories')
#         return ','.join(categories)

# class ExtraInfoForm(ModelForm):
#     categories = forms.ModelMultipleChoiceField(
#         queryset=None,
#         widget=forms.CheckboxSelectMultiple,
#         label="Select multiple options",
#         required=True,
#     )
#
#     def __init__(self, *args, **kwargs):
#         super(ExtraInfoForm, self).__init__(*args, **kwargs)
#         self.fields["categories"].queryset = self.get_dynamic_choices()
#
#     def get_dynamic_choices(self):
#         url = "http://discovery.local.overhang.io/api/v1/course_tags/"
#         username = "admin1"
#         password = "123456"
#         try:
#             response = requests.get(url, auth=HTTPBasicAuth(username, password))
#             if response.status_code == 200:
#                 data = response.json()
#                 choices = [(item["id"], item["name"]) for item in data]
#                 return choices
#             else:
#                 return [
#                     ("placeholder", "Завантаження категорій...")
#                 ]  # Повідомлення за замовчуванням
#         except requests.exceptions.RequestException:
#             return [
#                 ("placeholder", "Помилка при отриманні категорій")
#             ]  # Повідомлення за замовчуванням для будь-якого винятку
#
#     class Meta(object):
#         model = ExtraInfo
#         fields = ("categories",)
#         labels = {"categories": "Сategories"}
#         help_text = {"categories": "Сhoose your interests"}
