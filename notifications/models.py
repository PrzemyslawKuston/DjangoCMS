#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Notifications(models.Model):
	title = models.CharField(max_length=150, verbose_name="Tytuł")
	content = models.TextField(verbose_name="Wiadomość")
	viewed = models.BooleanField(default=False, verbose_name="Otwarta")
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

@receiver(post_save, sender=User)
def senb_welcome_message(sender, **kwargs):
	if kwargs.get('created', False):
		Notifications.objects.create(user=kwargs.get('instance'),
			title = "Witamy w naszym serwisie",
			content = "To jest powitanie",
			)
