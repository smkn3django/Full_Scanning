import os
import time
from django.core.management.base import BaseCommand
from scanmonitoring.models import MonitoringLog


class Command(BaseCommand):
    help = 'Monitors a folder for new files and logs total files to the database every 5 seconds'

    def handle(self, *args, **options):
        source_path = 'c://dms'  # Set your folder path here
        source_uncategories = 'c://dms'
        source_large_file= 'c://dms'
        source_miss_nip = 'c://dms'
        source_not_a_pdf = 'c://dms'
        source_doc_proceed = 'c://dms'
        source_doc_uploaded ='c://dms'

        self.stdout.write(self.style.SUCCESS(f'Starting to monitor folder: {source_path}'))

        while True:
            # Count total files in the folder
            total_files = len([f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))])
            
            total_uncategories = len([f for f in os.listdir(source_uncategories) if os.path.isfile(os.path.join(source_uncategories, f))])
            total_large_file= len([f for f in os.listdir(source_large_file) if os.path.isfile(os.path.join(source_large_file, f))])
            total_miss_nip = len([f for f in os.listdir(source_miss_nip) if os.path.isfile(os.path.join(source_miss_nip, f))])
            total_not_a_pdf = len([f for f in os.listdir(source_not_a_pdf) if os.path.isfile(os.path.join(source_not_a_pdf, f))])
            total_doc_proceed = len([f for f in os.listdir(source_doc_proceed) if os.path.isfile(os.path.join(source_doc_proceed, f))])
            total_doc_uploaded = len([f for f in os.listdir(source_doc_uploaded) if os.path.isfile(os.path.join(source_doc_uploaded, f))])

            # Log the total files and the current time to the database
            MonitoringLog.objects.create(total_files=total_files, total_uncategories = total_uncategories,
                                         total_large_file=total_large_file,total_miss_nip=total_miss_nip,
                                         total_not_a_pdf=total_not_a_pdf,total_doc_proceed=total_doc_proceed,
                                         total_doc_uploaded=total_doc_uploaded  )

            # Print a success message for each logging event
            self.stdout.write(self.style.SUCCESS(f'Total files: {total_files} at {time.strftime("%Y-%m-%d %H:%M:%S")}'))

            # Wait for 5 seconds before running the loop again
            time.sleep(5)
