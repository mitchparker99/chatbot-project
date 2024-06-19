from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import chatbot_response


class ChatbotAPIView(APIView):
    def post(self, request):
        user_message = request.data.get('message')
        response = chatbot_response(user_message)
        return Response({'response': response}, status=status.HTTP_200_OK)


def chat_view(request):
    return render(request, 'chatbot_app/chat.html')
