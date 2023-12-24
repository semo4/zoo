from django import forms
from django.contrib.auth.models import User


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class LoginForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
