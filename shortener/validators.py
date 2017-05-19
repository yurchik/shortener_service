from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
	url_validator = URLValidator()
	reg_val = value
	if "http" in value:
		new_value = reg_val
	else: 
		new_value = 'http://' + value
	try:
		url_validator(new_value)
	except:
		raise ValidationError("Invalide URL for this field!")
	return new_value

def validate_dot_com(value):
	if not '.com' in value:
		raise ValidationError("Invalide URL beacause it's not .com in it!")
	return value