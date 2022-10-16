from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('buscar/', views.searcher, name="searcher"),
    path('niñera/', views.perfil_niñera, name="perfilniñera"),
    path('cliente/', views.perfil_cliente, name="perfilcliente"),
    path('reg-cliente/<str:user>', views.register_cliente, name="reg-cliente"),
    path('reg-niñera/<str:user>', views.register_niñera, name="reg-niñera"),
    path('registro/', views.register, name="registro"),
    path('perfil/<str:user>', views.update_perfil, name='perfil'),
    path('<int:pk>/add-comment', views.crear_mensaje, name='crear_mensaje'),
    path('logueo/', views.logueo, name="logueo"),
    path('logout/', views.log_out, name="logout"),
    #path('delete_perfiles/<cliente_id>',views.delete_perfil,name='delete_perfil'),
    path('reservas/<int:id>',views.reserva_add,name="reservas"),
]

