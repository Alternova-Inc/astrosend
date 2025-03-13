from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('send/', views.send_secret, name='send'),
    path('history/', views.history, name='history'),
] 