from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    return render(request, 'a_rtchat/chat.html')