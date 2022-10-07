from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('reg-cliente/<str:user>', views.register_cliente, name="reg-cliente"),
    path('reg-niñera/<str:user>', views.register_niñera, name="reg-niñera"),
    path('registro/', views.register, name="registro"),
    path('logueo/', views.logueo, name="logueo"),
    path('logout/', views.log_out, name="logout")
]
