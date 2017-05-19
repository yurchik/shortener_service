from django.db import models
from django.conf import settings
# from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse

from .utils import code_generator, create_shortcode
from .validators import validate_dot_com, validate_url

SHORTCODE_MAX = getattr(settings, "SHORTCODES_MAX", 15)

class YurchikURLManager(models.Manager):

	def all(self, *args, **kwargs):
		qs_main = super(YurchikURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items=None):
		qs = YurchikURL.objects.filter(pk__gte=1)
		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
		new_codes = 0
		for q in qs:
			q.short_url = create_shortcode(q)
			print(q.id)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)

class YurchikURL(models.Model):
	url 		= models.CharField(max_length=220, validators=[validate_dot_com, validate_url])
	short_url 	= models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True) # every time the model is saved 
	timestamp 	= models.DateTimeField(auto_now_add=True) # every time the model is created 
	active		= models.BooleanField(default=True)
	
	objects = YurchikURLManager()

	def save(self, *args, **kwargs):
		if self.short_url == None or self.short_url == "":
			self.short_url = create_shortcode(self)
		if "http" not in self.url:
			self.url = "http://" + 	self.url
		super(YurchikURL, self).save(*args, **kwargs)


	def __str__(self):
		return str(self.url)

	def get_short_url(self):
		yurchik_url = reverse("scode", kwargs={ 'shortcode': self.short_url}, host="www", scheme='http', port='8000')
		return yurchik_url
