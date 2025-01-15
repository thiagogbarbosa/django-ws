from django.shortcuts import render

# Create your views here.

def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public-chat')
    return render(request, 'a_rtchat/chat.html')