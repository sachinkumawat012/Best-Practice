from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

# Create your models here.


class Student(models.Model):
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.student_name

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField(max_length=255)
    is_seen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()   #get all channel layer (group)
        notifications = Notification.objects.all().count()
        data = {
            "count":notifications,
            "current_notification":self.notification,
            "is_seen":self.is_seen
            }
        async_to_sync(channel_layer.group_send)(
            "test_consumer_group", {                        #call the group
                'type':'send_notification',                 #Name of that function to be called
                'value':json.dumps(data)
            }
        )
        super(Notification, self).save(*args, **kwargs)

