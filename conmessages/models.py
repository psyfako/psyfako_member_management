from django.db import models

from django.conf import settings

from django.db.models.signals import post_save
from django.dispatch import receiver

from twx.botapi import TelegramBot

mr_t = TelegramBot(settings.TELEGRAM_BOT_TOKEN)


class Channel (models.Model):
    name     = models.CharField(max_length=20)
    chat_id  = models.IntegerField()
    chat_url = models.URLField()
    
    def __str__(self):
        return self.name + ' ' + str(self.chat_id)


class Message (models.Model):
    channel   = models.ForeignKey(Channel, on_delete=models.SET_NULL, null=True, related_name="message")
    content   = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.channel) + ' | ' + self.content
     
@receiver(post_save, sender=Message)
def botMessage(instance, **kwargs):
    mr_t.send_message(instance.channel.chat_id, instance.content).wait()
    
    
#class Picture (models.Model):
#    pass
#
#
#@receiver(post_save, sender=Picture):
#def botMessage(instance, **kwargs):
#    mr_t.send_photo(chat_id, instance.photo, caption=None, reply_to_message_id=None).wait()
  
# ForeignKey stuff because the docu sucks .... 
# http://stackoverflow.com/a/8543956
    

    
    
    
