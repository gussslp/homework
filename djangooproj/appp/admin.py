from django.contrib import admin
from appp.models import ChatbotUser, MessageHistory


class ChatbotUsersAdmin(admin.ModelAdmin):
    ...
 
class MessagehistoryAdmin(admin.ModelAdmin):
    ...

admin.site.register(ChatbotUser,ChatbotUsersAdmin)
admin.site.register(MessageHistory,MessagehistoryAdmin)