from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat
import json
from django.views import View
# Create your views here.


# def chat_view(request):
#     if request.method == "GET":
#         chats = Chat.objects.all()
#         chat_list = []
#         for chat in chats:
#             chat_dict = {
#                 "name": chat.name,
#                 "message": chat.message,
#                 "created_at": chat.created_at
#             }
#             chat_list.append(chat_dict)
#             return JsonResponse(chat_list, safe=False)

#     if request.method == "POST":
#         data = json.loads(request.body)
#         Chat.objects.create(name=data["name"], message=data["message"])
#         return JsonResponse(data)


class ChatView(View):
    def get(self, request):
        chats = Chat.objects.all()
        chat_list = []
        for chat in chats:
            chat_dict = {
                "name": chat.name,
                "message": chat.message,
                "created_at": chat.created_at
            }
            chat_list.append(chat_dict)
        return JsonResponse(chat_list, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        Chat.objects.create(name=data["name"], message=data["message"])
        return JsonResponse(data)
