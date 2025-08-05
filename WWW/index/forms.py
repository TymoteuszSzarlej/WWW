from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Imię i nazwisko")
    email = forms.EmailField(label="Adres e-mail")
    message = forms.CharField(widget=forms.Textarea, label="Wiadomość")