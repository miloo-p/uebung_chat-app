from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from django.http import JsonResponse
from .models import Chat
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

@method_decorator(csrf_exempt, name='dispatch')
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
