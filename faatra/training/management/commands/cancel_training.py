from django.core.management.base import BaseCommand

from training.models import InformativeOffer

class Command(BaseCommand):
    help = 'Cancel informative offer'

    def handle(self, *args, **kwargs):
        from datetime import date
        today = date.today()
        query = InformativeOffer.objects.filter(due_date__lt=today)
        query.update(cancelled=True)