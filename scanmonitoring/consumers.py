import json
from channels.generic.websocket import AsyncWebsocketConsumer

class FileConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the 'file_updates' group
        await self.channel_layer.group_add("file_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard("file_updates", self.channel_name)

    async def send_new_file(self, event):
        # Send the data to WebSocket
        file_data = event['file_data']
        await self.send(text_data=json.dumps(file_data))
