from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=10)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    is_active = forms.BooleanField(label='Active', required=False)
