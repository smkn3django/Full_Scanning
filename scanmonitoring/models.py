from django.db import models

class FileRecord(models.Model):
    filename = models.CharField(max_length=255)
    source_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.filename} from {self.source_path}'

class MonitoringLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    total_files = models.IntegerField()
    total_uncategories = models.IntegerField()
    total_large_file= models.IntegerField()
    total_miss_nip = models.IntegerField()
    total_not_a_pdf = models.IntegerField()
    total_doc_proceed = models.IntegerField()
    total_doc_uploaded = models.IntegerField()

    def __str__(self):
        return f'{self.total_files} files at {self.timestamp}'