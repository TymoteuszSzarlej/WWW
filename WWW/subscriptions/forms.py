from django import forms
from .models import Subscription

class SubscriptionBuyForm(forms.Form):
    plan = forms.CharField(max_length=100)
    price = forms.IntegerField(min_value=0, help_text="Cena w groszach")

class SubscriptionExtendForm(forms.Form):
    extend_months = forms.IntegerField(min_value=1, label="Przedłuż o (miesiące)")

class SubscriptionDeleteForm(forms.Form):
    confirm = forms.BooleanField(label="Potwierdź usunięcie", required=True)