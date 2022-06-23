import json
import random
import threading
import time
import faker
from .models import *
from faker import Faker
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

fake=Faker()

class CreateStudentThread(threading.Thread):
    def __init__(self, total):
        self.total = total
            # Call the Thread class's init function
        threading.Thread.__init__(self)
    
    def run(self):

        try:
            print("Thread exicution start")
            channel_layer = get_channel_layer()
            current_total = 0

            for i in range(self.total):
                current_total+=1
                student_obj = Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10, 50),
                )
                channel_layer = get_channel_layer()   #get all channel layer (group)
                data = {
                    "id":current_total, 
                    "current_total":current_total,
                    "total":self.total,
                    "student_name":student_obj.student_name,
                    "student_age":student_obj.age,
                    "student_address":student_obj.address
                    }
                print(data)
                async_to_sync(channel_layer.group_send)(
                    "new_consumer_group", {                        #call the group
                        'type':'send_notification',                 #Name of that function to be called
                        'value':json.dumps(data)
                    }
                )
                # time.sleep(1)
        except Exception as e:
            print(e)