from django.urls import path
#from . import views
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('', publicaciones_view, name='dashboard_home'),
    path('publicaciones/', publicaciones_view, name='dashboard_publicaciones'),
    path('estadisticas/', estadisticas_view, name='dashboard_estadisticas'),
    path('top/', top_view, name='dashboard_top'),

    path('exportar-csv/', exportar_estadisticas_csv, name='exportar_estadisticas_csv'),
]
