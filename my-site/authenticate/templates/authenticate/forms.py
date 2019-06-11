from django.contrib.auth.forms import UserCreationForm
from django import forms
from django contrib.auth.models import

class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.Charfield(max_length=100)
	last_name = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2',}