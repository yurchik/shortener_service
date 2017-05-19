from django.db import models

from shortener.models import YurchikURL


class ClickEventManager(models.Manager):
	def create_event(self, instance):
		if isinstance(instance, YurchikURL):
			obj, created = self.get_or_create(yurchik_url=instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None


class ClickEvent(models.Model):
	yurchik_url = models.OneToOneField(YurchikURL)
	count 		= models.IntegerField(default=0)
	updated 	= models.DateTimeField(auto_now=True) 
	timestamp 	= models.DateTimeField(auto_now_add=True) 

	objects = ClickEventManager()

	def __str__(self):
		return "{url} clicked {count}".format(url=self.yurchik_url.url, count=self.count) 
