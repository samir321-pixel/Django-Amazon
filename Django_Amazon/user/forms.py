from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.forms import Form, CharField, EmailField, PasswordInput


class PostForm(forms.ModelForm):
    username = CharField()
    password = CharField(widget=PasswordInput)

    def clean_password_confirm(self):
        cleaned_data = super().clean()


from django import forms

class NameForm(forms.Form):
    username = CharField()
    password = CharField(widget=PasswordInput)
