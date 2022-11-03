import random
import vk_api
from base import *
from vk_api.longpoll import VkEventType, VkLongPoll
from config import TOKEN


class BaseServer:
    vk = vk_api.VkApi(token=TOKEN)
    longpoll = VkLongPoll(vk)

    def start(self, command_list: dict):
        self.commands = command_list
        for event in self.longpoll.listen():
            self.command_worker(event)
    
    def command_worker(self, event):
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                self.commands[event.text.lower()](event)


class UtilsServer(BaseServer):
    def send_msg(self, user_id, message):
        params = {
            "user_id": user_id,
            "message": message,
            "random_id": random.randint(1,10000)
        }
        self.vk.method("messages.send", params)
    

class Server(UtilsServer):
    def command_hi(self, event):
        self.send_msg(
            event.user_id,
            f"Привет!"
        )
    
    def command_monday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(monday)
        )
    
    def command_tuesday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(tuesday)
        )
    
    def command_wednesday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(wednesday)
        )
    
    def command_thursday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(thursday)
        )
    
    def command_friday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(friday)
        )
    
    def command_saturday(self, event):
        self.send_msg(
            event.user_id,
            "\n".join(saturday)
        )



