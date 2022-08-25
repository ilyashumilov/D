from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)
#
# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")
#
# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user

class reg_form(forms.Form):
    username = forms.CharField(label='username', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label="email", max_length=64)

class quest_form(forms.Form):
    company = forms.CharField(label='company', max_length=64)
    revenue = forms.CharField(label='revenue', max_length=64)
    fee1 = forms.CharField(label='fee1', max_length=64)
    fee2 = forms.CharField(label='fee2', max_length=64)
