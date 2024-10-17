import os
import time
from django.core.management.base import BaseCommand
from scanmonitoring.models import MonitoringLog


class Command(BaseCommand):
    help = 'Monitors a folder for new files and logs total files to the database every 5 seconds'

    def handle(self, *args, **options):
        source_path = 'Z:\\SMKN3 MANADO'  # Set your folder path here
        source_uncategories = 'Z:\\DOCUMENT_REJECTION\\UNCATEGORIES'
        source_large_file= 'Z:\\DOCUMENT_REJECTION\\LARGE'
        source_miss_nip = 'Z:\\DOCUMENT_REJECTION\\MISS_NIP'
        source_not_a_pdf = 'Z:\\DOCUMENT_REJECTION\\NOT_A_PDF'
        source_doc_proceed = 'Z:\\DOCUMENT_APPROVED'
        source_doc_uploaded ='Z:\\DOCUMENT_UPLOADED'

        self.stdout.write(self.style.SUCCESS(f'Starting to monitor folder: {source_path}'))

        while True:
            # Count total files in the folder
            # total_files = len([f for f in os.listdir(source_path) if os.path.isfile(os.path.join(source_path, f))])
            total_files = sum([len(files) for _, _, files in os.walk(source_path)])
            
            total_uncategories = sum([len(files) for _, _, files in os.walk(source_uncategories)])
            total_large_file= sum([len(files) for _, _, files in os.walk(source_large_file)])
            total_miss_nip = sum([len(files) for _, _, files in os.walk(source_miss_nip)])
            total_not_a_pdf = sum([len(files) for _, _, files in os.walk(source_not_a_pdf)])
            total_doc_proceed = sum([len(files) for _, _, files in os.walk(source_doc_proceed)])
            total_doc_uploaded = sum([len(files) for _, _, files in os.walk(source_doc_uploaded)])
            # total_doc_approved = sum([len(files) for _, _, files in os.walk(source_doc_approved)])

            # Log the total files and the current time to the database
            MonitoringLog.objects.create(total_files=total_files, 
                                         total_uncategories = total_uncategories,
                                         total_large_file=total_large_file,
                                         total_miss_nip=total_miss_nip,
                                         total_not_a_pdf=total_not_a_pdf,
                                         total_doc_proceed=total_doc_proceed,
                                         total_doc_uploaded=total_doc_uploaded)

            # Print a success message for each logging event
            self.stdout.write(self.style.SUCCESS(f'Total files: {total_files} at {time.strftime("%Y-%m-%d %H:%M:%S")}'))

            # Wait for 5 seconds before running the loop again
            time.sleep(1)
