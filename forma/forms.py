from django.forms import ModelForm

from app.models import Details
from forma.models import Forma

class CreateForma(ModelForm):
    class Meta:
            model = Forma
            fields = ["last_name", "first_name", "date", "car_name", "detail", "problem"]

    detail=Details.objects.filter(details_cars_id="1")