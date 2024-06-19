from django.urls import path
from .views import ChatbotAPIView, chat_view

urlpatterns = [
    path('api/chatbot/', ChatbotAPIView.as_view(), name='chatbot_api'),
    path('', chat_view, name='chat_view'),
]
