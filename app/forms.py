from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from app.models import Notation


class DateInput(forms.DateInput):
    input_type = 'date'


class NotationForm(ModelForm):
    reminder = forms.DateField(widget=DateInput)

    class Meta:
        model = Notation
        fields = ['title', 'text', 'reminder', 'category']

    def __init__(self, *args, **kwargs):
        super(NotationForm, self).__init__(*args, **kwargs)

        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'


class RegistrationForm(ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'

    def save(self, *args, **kwargs):
        self.instance.set_password(self.cleaned_data['password'])
        super().save(*args, **kwargs)


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)

        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'
