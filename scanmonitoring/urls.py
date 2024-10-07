from django.urls import path

from .views import monitoring_chart
from .views import index

app_name = 'scanmonitoring'
urlpatterns = [
    path("", index, name='index'),
    path("monitoring_chart", monitoring_chart, name='monitoring_chart')
]