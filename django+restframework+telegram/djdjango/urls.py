from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from rest_framework import routers
from appo import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()

router.register(r'ChatbotUser',views.ChatbotUserViewSet)

urlpatterns = [
    path('admin/',admin.site.urls),
    re_path(r'^',include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

router.register(r'MessageHistory',views.MessageHistoryViewSet)

urlpatterns = [
    path('admin/',admin.site.urls),
    re_path(r'^',include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
