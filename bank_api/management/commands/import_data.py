import csv
from django.core.management.base import BaseCommand
from ...models import Bank, Branch

class Command(BaseCommand):
    help = 'Import data from CSV into the database'

    def handle(self, *args, **options):
        csv_file_path = './bank_branches.csv'

        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                bank, _ = Bank.objects.get_or_create(name=row['bank_name'])
                Branch.objects.create(
                    ifsc=row['ifsc'],
                    bank=bank,
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state']
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))