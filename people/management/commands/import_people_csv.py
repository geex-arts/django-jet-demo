import csv
from django.core.management.base import NoArgsCommand, BaseCommand
from people.models import Company, County, City, State, Address, Person
from django.db import connection


class Command(BaseCommand):
    help = "Import data from csv"

    def add_arguments(self, parser):
        parser.add_argument('csv-file-path', type=str)

    def handle(self, *args, **options):
        cursor = connection.cursor()

        if connection.vendor == 'mysql':
            cursor.execute('SET FOREIGN_KEY_CHECKS = 0')
            cursor.execute('TRUNCATE TABLE `{0}`'.format(Company._meta.db_table))
            cursor.execute('TRUNCATE TABLE `{0}`'.format(County._meta.db_table))
            cursor.execute('TRUNCATE TABLE `{0}`'.format(City._meta.db_table))
            cursor.execute('TRUNCATE TABLE `{0}`'.format(State._meta.db_table))
            cursor.execute('TRUNCATE TABLE `{0}`'.format(Address._meta.db_table))
            cursor.execute('TRUNCATE TABLE `{0}`'.format(Person._meta.db_table))
            cursor.execute('SET FOREIGN_KEY_CHECKS = 1')
        else:
            Company.objects.all().delete()
            State.objects.all().delete()
            County.objects.all().delete()
            City.objects.all().delete()
            Address.objects.all().delete()
            Person.objects.all().delete()

        with open(options.get('csv-file-path'), 'rU') as f:
            FIRST_NAME_INDEX = 0
            LAST_NAME_INDEX = 1
            COMPANY_INDEX = 2
            ADDRESS_INDEX = 3
            CITY_INDEX = 4
            COUNTY_INDEX = 5
            STATE_INDEX = 6
            ZIP_INDEX = 7
            PHONE_INDEX = 8
            EMAIL_INDEX = 10
            WEB_INDEX = 11

            data = csv.reader(f)

            # IMPORT:
            # companies, states

            companies = {}
            states = {}

            f.readline()

            for row in data:
                if companies.get(row[COMPANY_INDEX]) is None:
                    companies[row[COMPANY_INDEX]] = Company(name=row[COMPANY_INDEX])

                if states.get(row[STATE_INDEX]) is None:
                    states[row[STATE_INDEX]] = State(name=row[STATE_INDEX])

            Company.objects.bulk_create(companies.values())
            State.objects.bulk_create(states.values())

            companies = dict(map(lambda v: (v.name, v), Company.objects.all()))
            states = dict(map(lambda v: (v.name, v), State.objects.all()))

            # IMPORT:
            # counties

            counties = {}

            f.seek(0)
            f.readline()

            for row in data:
                if counties.get(row[COUNTY_INDEX]) is None:
                    counties[row[COUNTY_INDEX]] = County(name=row[COUNTY_INDEX], state=states[row[STATE_INDEX]])

            County.objects.bulk_create(counties.values())

            counties = dict(map(lambda v: (v.name, v), County.objects.all()))

            # IMPORT:
            # cities

            cities = {}

            f.seek(0)
            f.readline()

            for row in data:
                if cities.get(row[CITY_INDEX]) is None:
                    cities[row[CITY_INDEX]] = City(name=row[CITY_INDEX], state=states[row[STATE_INDEX]], county=counties[row[COUNTY_INDEX]])

            City.objects.bulk_create(cities.values())

            cities = dict(map(lambda v: (v.name, v), City.objects.all()))

            # IMPORT:
            # addresses

            addresses = {}

            f.seek(0)
            f.readline()

            for row in data:
                if addresses.get(row[ADDRESS_INDEX]) is None:
                    addresses[row[ADDRESS_INDEX]] = Address(name=row[ADDRESS_INDEX], city=cities[row[CITY_INDEX]], zip=row[ZIP_INDEX])

            Address.objects.bulk_create(addresses.values())

            addresses = dict(map(lambda v: (v.name, v), Address.objects.all()))

            # IMPORT:
            # persons

            persons = []

            f.seek(0)
            f.readline()

            for row in data:
                persons.append(Person(
                    first_name=row[FIRST_NAME_INDEX],
                    last_name=row[LAST_NAME_INDEX],
                    address=addresses[row[ADDRESS_INDEX]],
                    company=companies[row[COMPANY_INDEX]],
                    phone=row[PHONE_INDEX],
                    email=row[EMAIL_INDEX],
                    web=row[WEB_INDEX]
                ))

            Person.objects.bulk_create(persons)

            print '%d persons have been imported' % len(persons)
