from django.db import models

# Create your models here.

class Conversation(models.Model):
    session_id = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rozmowa {self.id} ({self.session_id})"

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Wiadomość od {self.sender_name or 'Gość'}"

class Reply(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='replies')
    responder_name = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Odpowiedź od {self.responder_name or 'Zespół'}"

class Lead(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.SET_NULL, null=True, blank=True)
    service = models.CharField(max_length=100, blank=True)
    valuation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead: {self.name}"
