from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation, Message, Reply, Lead
from django.contrib import messages

def start_conversation(request):
    if request.method == 'POST':
        session_id = request.session.session_key or request.session.save()
        user = request.user if request.user.is_authenticated else None
        conversation = Conversation.objects.create(session_id=session_id, user=user)
        return redirect('conversation_detail', pk=conversation.pk)
    return render(request, 'contact/start_conversation.html')

def conversation_detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    messages_list = conversation.messages.all()
    replies_list = conversation.replies.all()
    return render(request, 'contact/conversation_detail.html', {
        'conversation': conversation,
        'messages': messages_list,
        'replies': replies_list,
    })

def send_message(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        content = request.POST.get('content', '')
        if content:
            Message.objects.create(
                conversation=conversation,
                sender_name=sender_name,
                email=email,
                phone=phone,
                content=content
            )
            messages.success(request, "Wiadomość wysłana.")
            return redirect('conversation_detail', pk=pk)
    return render(request, 'contact/send_message.html', {'conversation': conversation})

def add_lead(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk)
    if request.method == 'POST':
        service = request.POST.get('service', '')
        valuation = request.POST.get('valuation', None)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        Lead.objects.create(
            conversation=conversation,
            service=service,
            valuation=valuation if valuation else None,
            name=name,
            email=email,
            phone=phone
        )
        messages.success(request, "Lead zapisany.")
        return redirect('conversation_detail', pk=pk)
    return render(request, 'contact/add_lead.html', {'conversation': conversation})
