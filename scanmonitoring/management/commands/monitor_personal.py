import os
import time
from django.core.management.base import BaseCommand
from scanmonitoring.models import MonitoringPersonal

class Command(BaseCommand):
    help = 'Monitors a folder for new files and logs total files to the database every 5 seconds'

    def handle(self, *args, **options):
        source_ananda = 'Z:\\SMKN3 MANADO\Ananda'
        source_bagas = 'Z:\\SMKN3 MANADO\\Bagas'
        source_nia = 'Z:\\SMKN3 MANADO\\Nia'
        source_nathan = 'Z:\\SMKN3 MANADO\\Nathaniel'
        # put personal path

        self.stdout.write(self.style.SUCCESS(f'starting to monitor every peersonal'))

        while True:

            total_ananda = sum([len(files) for _, _, files in os.walk(source_ananda)])
            total_bagas = sum([len(files) for _, _, files in os.walk(source_bagas)])
            total_nia = sum([len(files) for _, _, files in os.walk(source_nia)])
            total_nathan = sum([len(files) for _, _, files in os.walk(source_nathan)])

            MonitoringPersonal.objects.create(
                ananda=total_ananda,
                bagas=total_bagas,
                nia=total_nia,
                nathan=total_nathan
            )


        self.stdout.write(self.style.SUCCESS(f'Personal Progress has been updated at {time.strftime("%Y-%m-%d %H:%M:%S")}'))

        time.sleep(5)