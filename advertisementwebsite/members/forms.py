from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse_lazy
from website.models import Profile

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control col-3',"id":"username"}))
    password1 = forms.CharField(max_length=30,label="Password", widget=forms.PasswordInput(attrs={'class':'form-control col-3',"id":"password1"}))
    password2 = forms.CharField(max_length=30,label="Confirm password" ,widget=forms.PasswordInput(attrs={'class':'form-control col-3',"id":"password2"}))

    class Meta:
        model = User
        fields = ('username','password1', 'password2')

    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 != password2:
                raise forms.ValidationError("The given passwords do not match")
        return password2
    
    def clean_username(self):
        username= self.cleaned_data.get("username")
        qs=User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("This user is already taken")

        return username

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