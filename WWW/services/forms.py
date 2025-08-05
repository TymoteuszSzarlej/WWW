from django import forms
from .models import Service

class FreeValuationForm(forms.Form):
    base_price = forms.DecimalField(label="Cena bazowa", max_digits=10, decimal_places=2)
    valuation_coeff = forms.DecimalField(label="Współczynnik wyceny", max_digits=4, decimal_places=2)

class ScheduleMeetingForm(forms.Form):
    name = forms.CharField(max_length=100, label="Imię i nazwisko")
    email = forms.EmailField(label="Adres e-mail")
    details = forms.CharField(widget=forms.Textarea, label="Szczegóły spotkania")