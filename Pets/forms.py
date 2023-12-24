from django import forms
from .models import Apply_adoption, Adoption_by_user


class Apply_adoption_form(forms.ModelForm):
    class Meta:
        model = Apply_adoption
        fields = ('pet_id', 'user_owner_id')
        widgets = {
            'pet_id': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'user_owner_id': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }


class AdoptionOfferForm(forms.ModelForm):
    class Meta:
        model = Adoption_by_user
        fields = ('owner', 'petName', 'petBirthdate',
                  'type', 'breed', 'petImage', 'description')
        widgets = {
            'owner': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'petName': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'petBirthdate': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'class': 'form-group'
                }
            ),
            'breed': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'petImage': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
