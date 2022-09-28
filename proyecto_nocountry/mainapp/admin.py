from django.contrib import admin
from .models import Niñera,Cliente,Reserva

class NiñeraAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ReservaAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Niñera,NiñeraAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Reserva,ReservaAdmin)

