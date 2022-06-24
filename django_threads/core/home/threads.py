import json
import random
import threading
import time
import faker
from .models import *
from faker import Faker


fake=Faker()

class CreateStudentThread(threading.Thread):
    def __init__(self, total):
        self.total = total
            # Call the Thread class's init function
        threading.Thread.__init__(self)
    
    def run(self):

        try:

            for i in range(self.total):
                print(i)
                student_obj = Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10, 50),
                )

        except Exception as e:
            print(e)