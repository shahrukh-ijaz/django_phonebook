from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddContactForm(forms.Form):
    first_name = forms.CharField(label='Enter firstname...', max_length=30, required=True)
    last_name = forms.CharField(label='Enter lastname...',  max_length=30, required=True)
    note = forms.CharField(label='Enter note...', max_length=30, required=True)
    dob = forms.DateField(required=True,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
    contact_number = forms.CharField(label='Enter contact number...', max_length=15, required=True)
    user_email = forms.EmailField(label='Enter contact email...', required=True)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Must enter a firstname')
    last_name = forms.CharField(max_length=30, required=True, help_text='Must enter a lastname')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
