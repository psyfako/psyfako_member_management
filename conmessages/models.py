from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from twx.botapi import TelegramBot


class Message (models.Model):
     content = models.TextField()
     time_sent = models.DateTimeField(auto_now_add=True)
     
@receiver(post_save, sender=Message)
def botMessage(instance, **kwargs):
    bot = TelegramBot('291219473:AAHBGYMCBfK4uD__P1DgC7VWt7gOqGzJW0o')
    chat_id = int(-1001078767317)
    bot.send_message(chat_id, instance.content).wait()