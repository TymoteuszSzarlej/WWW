from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation, Message, Reply, Lead
from django.contrib import messages

def contact(request):
    return render(request, 'contact/contact.html')