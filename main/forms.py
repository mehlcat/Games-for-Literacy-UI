from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(label='username', max_length=25, required=True)
	password = forms.CharField(label='password', max_length=25, required=True)
	firstname = forms.CharField(label='firstname', max_length=25, required=True)
	lastname = forms.CharField(label='lastname', max_length=25, required=True)
	email = forms.EmailField(label='email', max_length=25, required=True)

	def save(self):
		user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data["email"], self.cleaned_data["password1"])

		user.firstname = self.cleaned_data['firstname']
		user.lastname = self.cleaned_data['lastname']

		user.save()
		return user
