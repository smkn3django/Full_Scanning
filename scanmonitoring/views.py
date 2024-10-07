from django.shortcuts import render
from .models import FileRecord
from .models import MonitoringLog
from django.http import JsonResponse

# Create your views here.
def index(request):
    files = FileRecord.objects.all().order_by('-created_at')  # Get all files, ordered by creation date
    total_files = files.count()
    context = {
        'files': files,
        'total_files': total_files
    }
    return render(request, 'scanmonitoring/index.html', context)

def monitoring_chart(request):
    logs = MonitoringLog.objects.all().order_by('timestamp')
    timestamps = [log.timestamp.strftime('%Y-%m-%d %H:%M:%S') for log in logs]
    total_files = [log.total_files for log in logs]
    
    data = {
        'timestamps': timestamps,
        'total_files': total_files,
    }
    
    return JsonResponse(data)