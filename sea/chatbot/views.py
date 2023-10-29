from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

#@login_required
def chatbot(request):
    return render(request, 'chatbot/chatbot.html')

# write the function to collect the message from backend which is from jquery and send some response to the jquery

def message_handle(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        response_data = {'reply': 'The generated promt will be send to this location we need to only integrate it, all ther things are already ready'}
        return JsonResponse(response_data)
    else:
        return render(request, 'chatbot/chatbot.html')