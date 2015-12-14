from django.forms import ModelForm
from forma.models import Forma

class CreateForma(ModelForm):
    class Meta:
            model = Forma
            fields = ["last_name", "first_name", "date", "car_name", "detail", "problem"]