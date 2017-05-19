import random
import string

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODES_MIN", 6)
# from shortener.models import YurchikURL

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=SHORTCODE_MIN):
	new_code = code_generator(size=size)
	Klass = instance.__class__
	qs_exist = Klass.objects.filter(short_url=new_code).exists()
	if qs_exist:
		return create_shortcode(size=size)
	return new_code

