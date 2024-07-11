from django.contrib import admin

# Register your models here.
from .models import (
    TrackingCampos,TrackingCliente,
    TrackingDestinatarios,TrackingEstados,TrackingManifiesto,TrackingAdjuntos)

admin.site.register(TrackingCampos)
admin.site.register(TrackingCliente)
admin.site.register(TrackingEstados)
admin.site.register(TrackingDestinatarios)
admin.site.register(TrackingManifiesto)
admin.site.register(TrackingAdjuntos)