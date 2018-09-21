from django import forms
from django.forms import ModelForm
from books.models import Author


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = "__all__"


class AuthorSearchForm(forms.Form):
    name = forms.CharField(max_length=20)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
