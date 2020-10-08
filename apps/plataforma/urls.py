from django.urls import path

from apps.plataforma.views import Dashboard

urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
