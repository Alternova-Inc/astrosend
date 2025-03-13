from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('verify-code/', views.verify_code, name='verify_code'),
] 