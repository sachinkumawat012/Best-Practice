from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = "test_consumer_room"
        self.room_group_name = "test_consumer_group"
        # add room and group in the  channel layer
        async_to_sync(self.channel_layer.group_add)(  
            self.room_group_name,
            self.channel_name
        )
        self.accept()    # for accept connection 
        self.send(text_data=json.dumps({'status':'conneted'}))    #send data from backend

    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status':'We got you'}))

    def disconnect(self, *args, **kwargs):
        print("Disconnected")
        # self.send(text_data=json.dumps({"status":'successfully disconnected'}))

    def send_notification(self, event):
        print(event)
        data = json.loads(event.get("value"))
        self.send(text_data=json.dumps({'paylod':data}))


class NewConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = "new_consumer_room"
        self.room_group_name = "new_consumer_group"
        
        await(self.channel_layer.group_add)(  
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({'status':"New connection"}))
   
    async def receive(self, text_data):
        print(text_data)
        await self.send(text_data=json.dumps({'status':'We got you'}))

    async def disconnect(self, *args, **kwargs):
        print("Disconnected")
        # self.send(text_data=json.dumps({"status":'successfully disconnected'}))

    async def send_notification(self, event):
        data = json.loads(event.get("value"))
        await self.send(text_data=json.dumps({'paylod':data}))
