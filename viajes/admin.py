from django.contrib import admin

# Register your models here.
from .models import (
    Grupo,
    Catalogo,
    Articulo
)

admin.site.register(Grupo)
admin.site.register(Catalogo)
admin.site.register(Articulo)
