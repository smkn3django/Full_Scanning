from django.urls import path

from .views import monitoring_chart
from .views import index
from .views import api_top_ten
from .views import dashboard_page
from .views import dashboard_view

app_name = 'scanmonitoring'
urlpatterns = [
    path("", index, name='index'),
    path("monitoring_chart", monitoring_chart, name='monitoring_chart'),
    path("api_top_ten", api_top_ten, name='api_top_ten'),
    path('dashboard',dashboard_page, name='dashboard' ),
    path('dashboard2',dashboard_view, name='dashboard2')

]