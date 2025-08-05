from django import forms
from .models import Message, Reply, Lead

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender_name', 'email', 'phone', 'content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['responder_name', 'content']

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone', 'company', 'message']