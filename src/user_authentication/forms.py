from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()
class SignUpForm(UserCreationForm):
  	first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
  	last_name  = forms.CharField(max_length=30, required=False, help_text='Optional')
  	email 	   = forms.EmailField(max_length=54, help_text='Required')
  	photo 	   = forms.ImageField(required=False, help_text='Optional')
  	class Meta:
  		model = User
  		fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2',
  				  'gender', 'photo', 'user_note', )