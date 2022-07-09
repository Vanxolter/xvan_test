from django import forms

from mainapp.models import My_links


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class Authorization(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class LinksForm(forms.ModelForm):
    class Meta:
        model = My_links
        fields = ["long_link"]