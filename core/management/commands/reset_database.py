from django.core.management import call_command, BaseCommand


class Command(BaseCommand):
    help = 'Resets database'

    def handle(self, *args, **options):
        call_command('flush', '--noinput')
        call_command('loaddata', 'core/fixtures/initial_data.json')
        call_command('loaddata', 'editors/fixtures/initial_data.json')
        call_command('loaddata', 'menu/fixtures/initial_data.json')
        call_command('loaddata', 'people/fixtures/initial_data.json')
