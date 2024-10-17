from django.contrib import admin
from .models import MonitoringLog 
from .models import MonitoringPersonal
# Register your models here.


admin.site.register(MonitoringLog)
admin.site.register(MonitoringPersonal)