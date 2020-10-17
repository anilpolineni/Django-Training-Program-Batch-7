from django.forms import ModelForm
from FirstApp.models import Movies

class MoviesForm(ModelForm):
	class Meta:
		model=Movies
		fields="__all__"

