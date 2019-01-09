from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','name': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(
                                attrs={'class': 'form-control','name': 'password'}))
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput,label="Leave empty")





    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError("honeypot should be left empty")

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) == 0:
            raise forms.ValidationError("Invalid username or password")
            
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) == 0:
            raise forms.ValidationError("Invalid username or password")



class UserSignUpForm(UserCreationForm):
    class Meta():
        fields = ('username','first_name','last_name','email','password1','password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = 'username'
        self.fields['first_name'].label = 'first name'
        self.fields['last_name'].label = 'last name'
        self.fields['email'].label = 'email'
        self.fields['password1'].label = 'password'
        self.fields['password1'].label = 'Confirm password'

        self.fields['username'].widget = forms.TextInput(attrs= {
            'placeholder':'username',
            'class':'form-control'
        })

        self.fields['first_name'].widget = forms.TextInput(attrs= {
            'placeholder':'first name',
            'class':'form-control'
        })

        self.fields['last_name'].widget = forms.TextInput(attrs= {
            'placeholder':'last name',
            'class':'form-control'
        })

        self.fields['email'].widget = forms.EmailInput(attrs= {
            'placeholder':'email address',
            'class':'form-control'
        })

        self.fields['password1'].widget = forms.PasswordInput(attrs= {
            'placeholder':'password',
            'class':'form-control'
        })

        self.fields['password2'].widget = forms.PasswordInput(attrs= {
            'placeholder':'confirm password',
            'class':'form-control'
        })

            

