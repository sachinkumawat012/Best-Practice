from django.http import JsonResponse
from django.shortcuts import render
import  time
import json
from .threads import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from requests import request

# Create your views here.


async def home(request):
    # for i in range(1,11):
    #     channel_layer = get_channel_layer()   #get all channel layer (group)
    #     data = {
    #         "count":i
    #         }
    #     await(channel_layer.group_send)(
    #         "new_consumer_group", {                        #call the group
    #             'type':'send_notification',                 #Name of that function to be called
    #             'value':json.dumps(data)
    #         }
    #     )
    #     time.sleep(1)
    return render(request, 'home.html')


def generate_student_data(request):
    total = request.GET.get("total")
    CreateStudentThread(int(total)).start()
    return JsonResponse({"status":200})