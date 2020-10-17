from django.forms import ModelForm
from .models import UserRegister


class RegisterForm(ModelForm):
	class Meta:

		model=UserRegister
		fields="__all__"