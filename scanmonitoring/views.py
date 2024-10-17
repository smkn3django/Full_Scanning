from django.shortcuts import render
from .models import FileRecord
from .models import MonitoringLog
from .models import MonitoringPersonal
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

def dashboard_view(request):
    latest_stat = MonitoringLog.objects.latest('timestamp')  # Get the most recent entry
    context = {
        'latest_stat': latest_stat,
    }
    return render(request, 'scanmonitoring\dashboard2.html', context)

def dashboard3_view(request):
    latest_stat = MonitoringLog.objects.latest('timestamp')  # entry for monitoringLog
    latest_personal = MonitoringPersonal.objects.latest('jedawaktu')
    context = {
        'latest_stat': latest_stat,
        'latest_personal': latest_personal
    }
    
    return render(request, 'scanmonitoring\dashboard3.html', context)

def dashboard_page(request):
    stats = MonitoringLog.objects.order_by('-timestamp')[:10]  # Fetch last 10 entries for the cards
    chart_data = MonitoringLog.objects.order_by('timestamp')  # Fetch all data for the chart

    context = {
        'stats': stats,
        'chart_data': chart_data,
    }
    return render(request, 'scanmonitoring\dashboard.html',context)

def api_top_ten(request):
    stats = MonitoringLog.objects.order_by('-timestamp')[:10]  # Fetch last 10 entries for the cards
    chart_data = MonitoringLog.objects.order_by('timestamp')  # Fetch all data for the chart

    return JsonResponse(stats)


def monitoring_chart(request):
    logs = MonitoringLog.objects.all().order_by('-timestamp')[:100][::-1]
    timestamps = [log.timestamp.strftime('%Y-%m-%d %H:%M:%S') for log in logs]
    total_files = [log.total_files for log in logs]
    total_uncategories =[log.total_uncategories for log in logs]
    total_large_file= [log.total_large_file for log in logs]
    total_miss_nip = [log.total_miss_nip for log in logs]
    total_not_a_pdf = [log.total_not_a_pdf for log in logs]
    total_doc_proceed =[log.total_doc_proceed for log in logs]
    total_doc_uploaded = [log.total_doc_uploaded for log in logs]
    
    data = {
        'timestamps': timestamps,
        'total_files': total_files,
        'total_uncategories' : total_uncategories,
        'total_large_file': total_large_file,
        'total_miss_nip' : total_miss_nip,
        'total_not_a_pdf' : total_not_a_pdf,
        'total_doc_proceed' : total_doc_proceed,
        'total_doc_uploaded' : total_doc_uploaded,

    }
    
    return JsonResponse(data)