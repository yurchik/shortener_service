from django.core.management.base import BaseCommand, CommandError
from shortener.models import YurchikURL 

class Command(BaseCommand):
    help = 'Refreshing all YurchikURLs short_urls'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        return YurchikURL.objects.refresh_shortcodes()