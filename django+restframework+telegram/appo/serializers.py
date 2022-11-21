from .models import ChatbotUser, MessageHistory
from rest_framework import serializers

class ChatbotUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatbotUser
        fields = ('chat_id','full_name','username','language_code','reg_date')
        
class MessageHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MessageHistory
        fields = ('message_id','chat_id','full_name','username','date','text')
        