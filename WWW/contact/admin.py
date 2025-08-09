from django.contrib import admin
from .models import Conversation, Message, Reply, Lead

# Register your models here.
admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(Reply)
admin.site.register(Lead)