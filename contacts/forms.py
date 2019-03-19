from django import forms


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
