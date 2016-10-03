from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(required=True, max_length=45)
	password = forms.CharField(required=True)