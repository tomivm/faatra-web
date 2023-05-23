from django.core.management.base import BaseCommand

from training.models import InformativeOffer

class Command(BaseCommand):
    help = 'Cancel informative offer'

    def handle(self, *args, **kwargs):
        from datetime import datetime
        now = datetime.now()
        query = InformativeOffer.objects.filter(due_date__lte=now)
        query.update(cancelled=True)