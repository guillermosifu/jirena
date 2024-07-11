from django.db import models

class Ciudades(models.Model):
    nombre = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'ciudades'


class Clientes(models.Model):
    nombre = models.CharField(max_length=200)
    ruc = models.CharField(max_length=11)
    estado = models.IntegerField()
    rfuser_cre = models.IntegerField()
    date_added = models.DateField()
    val = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clientes'

    def __str__(self):
        return self.nombre


class Conductores(models.Model):
    licencia = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField()
    rfuser_cre = models.IntegerField()
    date_added = models.DateField()
    dni = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'conductores'


class Departamentos(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.IntegerField()
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'departamentos'


class Direcciones(models.Model):
    direccion = models.CharField(max_length=500)
    ref = models.CharField(max_length=300)
    rfcliente = models.IntegerField()
    estado = models.IntegerField()
    fecha = models.DateField()
    coordenadas = models.CharField(max_length=300)
    zona = models.CharField(max_length=50)
    rfuser_cre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'direcciones'


class Distritos(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField()
    fecha = models.DateField()
    rf_prov = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'distritos'
        
class Estadoguia(models.Model):
    nombre = models.CharField(max_length=20)
    abrev = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'estadoguia'


class Estados(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estados'

class Vehiculos(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    tipo_unidad = models.CharField(max_length=50)
    perfil = models.CharField(max_length=50, db_collation='utf8_spanish_ci')
    gal_tanque1 = models.IntegerField()
    gal_tanque2 = models.IntegerField()
    gal_total = models.IntegerField()
    estado = models.IntegerField()
    rfuser_cre = models.IntegerField()
    date_added = models.DateField()
    configuracion = models.CharField(max_length=5)
    mtc = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'vehiculos'



####################### NUEVOS ###############

# Create your models here.
class Grupo(models.Model):
    codigo = models.CharField(max_length=50,unique=True,null=True)
    descripcion = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.descripcion
    
class Catalogo(models.Model):
    codigo = models.CharField(max_length=255,unique=True)
    descripcion = models.CharField(max_length=255)
    grupo = models.ForeignKey(Grupo,on_delete=models.RESTRICT)
    estado = models.IntegerField(default=1)
    
    def __str__(self):
        return self.descripcion
    

class Articulo(models.Model):
    descripcion = models.CharField(max_length=255)
    catalogo = models.ForeignKey(Catalogo,on_delete=models.RESTRICT)
    estado = models.IntegerField(default=1)
    
    def __str__(self):
        return self.descripcion
    
    
    
    