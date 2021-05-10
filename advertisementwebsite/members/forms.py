from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
from website.models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'class':'form-control', 'default':'', 'type':'hidden'}), required=False)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'default':'', 'type':'hidden'}), required=False)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'default':'', 'type':'hidden'}), required=False)
    class Meta:
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'surname', 'profile_picture', 'phone', 'email', 'city')
        widgets = {
                'name': forms.TextInput(attrs={'class':'form-control'}),
                'surname': forms.TextInput(attrs={'class':'form-control'}),
                'phone': forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'}),
                'city': forms.TextInput(attrs={'class':'form-control'}),
        }