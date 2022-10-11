from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('buscar/', views.searcher, name="searcher"),
    path('niñera/', views.perfil_niñera, name="perfilniñera"),
    path('cliente/', views.perfil_cliente, name="perfilcliente")
]
