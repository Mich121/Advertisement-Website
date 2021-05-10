from django import forms
from .models import Advertisement

class AddAdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'image', 'price', 'body', 'owner')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'owner': forms.TextInput(attrs={'class':'form-control', 'id':'elder', 'type':'hidden'}),
        } 

class EditAdvertForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'image', 'price', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
        }