from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analitics.models import ClickEvent

from .models import YurchikURL
from .forms import SubmitUrlForm

class HomeView(View):
	def get(self, request, *arg, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			'title' : 'Yurchik.com',
			'form' : the_form,
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *arg, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			'title' : 'Yurchik.com',
			'form' : form,
		}
		template = "shortener/home.html"
		if form.is_valid():
			print(form.cleaned_data.get("url"))
			new_url = form.cleaned_data.get("url")
			obj, created = YurchikURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj, #17014
				"created": created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already_exists.html"
		
		return render(request, template, context)

class URLRedirectView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(YurchikURL, short_url=shortcode)
		# save item
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)