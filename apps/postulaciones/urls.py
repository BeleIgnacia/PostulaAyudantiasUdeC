from django.urls import path
from apps.postulaciones.views import despliega_ofertas_ayudantias
urlpatterns = [
path('ofertas_ayudantias/', despliega_ofertas_ayudantias.as_view(),name= 'listar_ofertas')
]