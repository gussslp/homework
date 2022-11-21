from django.shortcuts import render
from .models import ChatbotUser, MessageHistory
from rest_framework import viewsets
from .serializers import ChatbotUserSerializer
from .serializers import MessageHistorySerializer

class ChatbotUserViewSet(viewsets.ModelViewSet):
    queryset = ChatbotUser.objects.all().order_by('-chat_id')
    serializer_class = ChatbotUserSerializer
    
class MessageHistoryViewSet(viewsets.ModelViewSet):
    queryset = MessageHistory.objects.all().order_by('-message_id')
    serializer_class = MessageHistorySerializer