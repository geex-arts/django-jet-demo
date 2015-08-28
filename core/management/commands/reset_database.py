from django.core.management import call_command, BaseCommand


class Command(BaseCommand):
    help = 'Resets database'

    def handle(self, *args, **options):
        call_command('flush', '--noinput')

