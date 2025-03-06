from django.forms import ModelForm, NumberInput
from .models import Compra

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ['nombret','numerot','mest','annot','cvv',]

