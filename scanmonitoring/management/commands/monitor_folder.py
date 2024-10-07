import os
import time
from django.core.management.base import BaseCommand
from scanmonitoring.models import MonitoringLog

class Command(BaseCommand):
    help = 'Monitors a folder for new files and logs total files to the database every 5 seconds'

    def handle(self, *args, **options):
        source_path = 'c://dms'  # Set your folder path here

        self.stdout.write(self.style.SUCCESS(f'Starting to monitor folder: {source_path}'))

        while True:
            # Count total files in the folder
            total_files = len([f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))])
            
            # Log the total files and the current time to the database
            MonitoringLog.objects.create(total_files=total_files)

            # Print a success message for each logging event
            self.stdout.write(self.style.SUCCESS(f'Total files: {total_files} at {time.strftime("%Y-%m-%d %H:%M:%S")}'))

            # Wait for 5 seconds before running the loop again
            time.sleep(5)
