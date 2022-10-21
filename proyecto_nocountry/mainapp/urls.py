from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('buscar/', views.searcher, name="searcher"),
    path('profiles/<id>', views.profiles, name="profiles"),
    path('reg-cliente/<str:user>', views.register_cliente, name="reg-cliente"),
    path('reg-niñera/<str:user>', views.register_niñera, name="reg-niñera"),
    path('registro/', views.register, name="registro"),
    path('perfil/<str:user>', views.update_perfil, name='perfil'),
    path('logueo/', views.logueo, name="logueo"),
    path('logout/', views.log_out, name="logout"),
    path('delete_perfil/<str:user>',views.delete_perfil,name='delete_perfil'),
    path('welcome/', views.login_landing, name="welcome"),
]
