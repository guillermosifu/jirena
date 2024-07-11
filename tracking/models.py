from django.db import models

# Create your models here.

class Usuarios(models.Model):
    ced = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    usu = models.CharField(unique=True, max_length=255)
    con = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=250)
    despacho = models.IntegerField()
    seguimiento = models.IntegerField()
    confirma_guia = models.IntegerField()
    email = models.CharField(max_length=100, db_collation='utf8_unicode_ci')
    forgot_pass_identity = models.CharField(max_length=32, db_collation='utf8_unicode_ci', blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    status = models.CharField(max_length=1, db_collation='utf8_unicode_ci')
    phone = models.CharField(max_length=15, db_collation='utf8_unicode_ci')
    balotario = models.IntegerField()
    maestro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'
        
class Pesos(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    rfuser_cre = models.IntegerField()
    fecha_cre = models.DateField()
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pesos'

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

class Manifiestos(models.Model):
    nombre = models.IntegerField()
    curso = models.CharField(max_length=20, db_collation='utf8_spanish_ci')
    estado = models.CharField(max_length=2, db_collation='utf8_spanish_ci')
    rfuser_creacion = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='rfuser_creacion')
    fecha_creacion = models.DateField()
    rfuser_mod = models.IntegerField()
    fecha_mod = models.DateField()
    rfuser_elim = models.IntegerField()
    fecha_elim = models.DateField()
    obs = models.CharField(max_length=500)
    serie = models.CharField(max_length=3)
    numero = models.IntegerField()
    hora_creacion = models.TimeField()
    rfcliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='rfcliente')
    rfdir1 = models.IntegerField()
    rfdir2 = models.IntegerField()
    letra = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'manifiestos'
        

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


class Viajes(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'viajes'
        
class Grifos(models.Model):
    codigo = models.IntegerField()
    estacion = models.CharField(max_length=100)
    rfprov = models.IntegerField()
    direccion = models.CharField(max_length=500)
    urb = models.CharField(max_length=30)
    distrito = models.CharField(max_length=300)
    provincia = models.CharField(max_length=100)
    dpto = models.CharField(max_length=100)
    sistema = models.CharField(max_length=50)
    glp = models.CharField(db_column='GLP', max_length=1)  # Field name made lowercase.
    gnv = models.CharField(db_column='GNV', max_length=1)  # Field name made lowercase.
    g98 = models.CharField(db_column='G98', max_length=1)  # Field name made lowercase.
    g97 = models.CharField(db_column='G97', max_length=1)  # Field name made lowercase.
    g95 = models.CharField(db_column='G95', max_length=1)  # Field name made lowercase.
    g90 = models.CharField(db_column='G90', max_length=1)  # Field name made lowercase.
    g84 = models.CharField(db_column='G84', max_length=1)  # Field name made lowercase.
    d2 = models.CharField(db_column='D2', max_length=1)  # Field name made lowercase.
    estado = models.IntegerField()
    rfuser_cre = models.IntegerField()
    fechareg = models.DateField()
    tienda = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'grifos'

class Tramos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=255)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='cliente')
    descrip = models.CharField(max_length=255)
    fechan = models.DateField()
    bultos = models.CharField(max_length=20)
    curso = models.ForeignKey(Manifiestos, models.DO_NOTHING, db_column='curso')
    estado = models.CharField(max_length=2)
    rfconductor = models.IntegerField()
    peso = models.ForeignKey('Pesos', models.DO_NOTHING, db_column='peso')
    despach = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='despach')
    galactual = models.IntegerField()
    galnuevo = models.IntegerField()
    viaje = models.IntegerField()
    manif = models.CharField(max_length=20)
    ntramo = models.IntegerField()
    rfuser_creacion = models.IntegerField()
    fecha_creacion = models.DateField()
    rfuser_mod = models.IntegerField()
    fecha_mod = models.DateField()
    rfuser_elim = models.IntegerField()
    fecha_elim = models.DateField()
    placa_camion = models.CharField(max_length=10)
    placa_remolcador = models.CharField(max_length=10)
    placa_remolque = models.CharField(max_length=10)
    placa_camioneta = models.CharField(max_length=15)
    rfgrifo = models.ForeignKey(Grifos, models.DO_NOTHING, db_column='rfgrifo')
    rfruta = models.IntegerField()
    recorrido = models.IntegerField()
    kmactual = models.IntegerField()
    idauto = models.IntegerField()
    horasal = models.TimeField()
    fechalleg = models.DateField()
    horalleg = models.TimeField()
    rfrutaf = models.IntegerField()
    rfdir1 = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='rfdir1',related_name='rfdir1')
    rfdir2 = models.ForeignKey(Direcciones, models.DO_NOTHING, db_column='rfdir2',related_name='rfdir2')
    fechasal_r = models.DateField()
    horasal_r = models.TimeField()
    fechalleg_r = models.DateField()
    horalleg_r = models.TimeField()
    img_ori = models.CharField(max_length=300)
    img_dur = models.CharField(max_length=300)
    img_des = models.CharField(max_length=300)
    hoja_ruta = models.CharField(max_length=300)
    cod_eval_ssoma = models.CharField(max_length=20)
    rfconductor2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tramos'


class TramosDet(models.Model):
    rfcab_tramo = models.IntegerField()
    pcamion = models.CharField(max_length=10)
    premolcador = models.CharField(max_length=10)
    premolque = models.CharField(max_length=10)
    pcamioneta = models.CharField(max_length=10)
    rfconductor = models.IntegerField()
    rfuser_cre = models.IntegerField()
    fecha_cre = models.DateField()
    rfuser_mod = models.IntegerField()
    fecha_mod = models.DateField()
    rfuser_eli = models.IntegerField()
    fecha_eli = models.DateField()
    rfestado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tramos_det'       

class Guiarem(models.Model):
    serie = models.CharField(max_length=10)
    numero = models.CharField(max_length=20)
    idtramo = models.ForeignKey('Tramos', models.DO_NOTHING, db_column='idtramo',related_name='guiasrem')
    fecha = models.DateField()
    estado = models.CharField(max_length=1)
    rfuser_creacion = models.IntegerField()
    fecha_creacion = models.DateField()
    rfuser_mod = models.IntegerField()
    fecha_mod = models.DateField()
    rfuser_elim = models.IntegerField()
    fecha_elim = models.DateField()
    rfserie_trans = models.CharField(max_length=15)
    rfnum_trans = models.CharField(max_length=15)
    manif = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'guiarem'


class Guiatrans(models.Model):
    serie = models.CharField(max_length=4, db_collation='utf8_spanish_ci')
    numero = models.CharField(max_length=8, db_collation='utf8_spanish_ci')
    idtramo = models.ForeignKey('Tramos', models.DO_NOTHING, db_column='idtramo',related_name='guiastran')
    conductor = models.ForeignKey(Conductores, models.DO_NOTHING, db_column='conductor')
    copiloto = models.CharField(max_length=80, db_collation='utf8_spanish_ci')
    observacion = models.CharField(max_length=300, db_collation='utf8_spanish_ci')
    fecha = models.DateField()
    estado = models.CharField(max_length=1, db_collation='utf8_spanish_ci')
    rfestguia = models.IntegerField()
    rfestguia_ult = models.ForeignKey(Estadoguia, models.DO_NOTHING, db_column='rfestguia_ult')
    rfuser_creacion = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='rfuser_creacion')
    fecha_creacion = models.DateField()
    rfuser_mod = models.IntegerField()
    fecha_mod = models.DateField()
    rfuser_elim = models.IntegerField()
    fecha_elim = models.DateField()
    rfuser_est = models.IntegerField()
    fecha_est = models.DateField()
    manif = models.CharField(max_length=20, db_collation='utf8_spanish_ci')
    tipodoc = models.IntegerField()
    guia = models.CharField(max_length=15, db_collation='utf8_spanish_ci')
    hora_reg = models.TimeField()
    hora_mod = models.TimeField()
    hora_eli = models.TimeField()
    hora_est = models.TimeField()
    conformidad = models.IntegerField()
    fecha_confor = models.DateField()
    cotizacion = models.IntegerField()
    cod_facturar = models.IntegerField()
    fecha_facturar = models.DateField()
    f_rec_merca = models.DateField()
    f_conf_merca = models.DateField()
    f_ent_com = models.DateField()
    rfuser_confor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guiatrans'

from django.contrib.auth.models import User

class TrackingCliente(models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User,on_delete=models.RESTRICT)
    
    class Meta:
        db_table = 'tracking_cliente'

    def __str__(self):
        return self.cliente.nombre

    
class TrackingCampos(models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=255,null=True)
    campo = models.CharField(max_length=255,null=True)
    tipo = models.CharField(max_length=255,null=True)
    
    class Meta:
        db_table = 'tracking_campos'

    def __str__(self):
        return self.nombre
    

class TrackingEstados(models.Model):
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tracking_estados'

    def __str__(self):
        return self.descripcion

class TrackingDestinatarios(models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.DO_NOTHING)
    ruc = models.CharField(max_length=20,blank=True)
    nombre = models.CharField(max_length=255)
    direccion = models.TextField(blank=True)
    coordenadas = models.CharField(max_length=20,blank=True)

    class Meta:
        managed = False
        db_table = 'tracking_destinatarios'

    def __str__(self):
        return self.nombre

class TrackingRegistros(models.Model):
    tramo = models.OneToOneField(Tramos,on_delete=models.DO_NOTHING,related_name='tracking')
    destinatario = models.ForeignKey(TrackingDestinatarios,on_delete=models.RESTRICT,null=True)
    estado = models.ForeignKey(TrackingEstados,on_delete=models.RESTRICT,null=True)
    glosa1 = models.CharField(max_length=255,null=True)
    glosa2 = models.CharField(max_length=255,null=True)
    glosa3 = models.CharField(max_length=255,null=True)
    glosa4 = models.CharField(max_length=255,null=True)
    glosa5 = models.CharField(max_length=255,null=True)
    glosa6 = models.CharField(max_length=255,null=True)
    glosa7 = models.CharField(max_length=255,null=True)
    glosa8 = models.CharField(max_length=255,null=True)
    glosa9 = models.CharField(max_length=255,null=True)
    glosa10 = models.CharField(max_length=255,null=True)
    
    class Meta:
        db_table = 'tracking_registros'
        
class TrackingManifiesto(models.Model):
    id = models.BigAutoField(primary_key=True)
    guia_remision_serie = models.CharField(max_length=255, blank=True, null=True)
    guia_remision_nro = models.BigIntegerField(blank=True, null=True)
    guia_transportista_serie = models.CharField(max_length=255, blank=True, null=True)
    guia_transportista_nro = models.BigIntegerField(blank=True, null=True)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    sales_order = models.CharField(max_length=255, blank=True, null=True)
    orden_compra = models.CharField(max_length=255, blank=True, null=True)
    unidad_minera = models.CharField(max_length=255, blank=True, null=True)
    punto_origen = models.CharField(max_length=255, blank=True, null=True)
    punto_destino = models.CharField(max_length=255, blank=True, null=True)
    peso_total = models.CharField(max_length=255, blank=True, null=True)
    nro_bultos = models.CharField(max_length=255, blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    fecha_inicio_traslado = models.DateField(blank=True, null=True)
    fecha_entrega_programada = models.DateField(blank=True, null=True)
    fecha_entrega_real = models.DateField(blank=True, null=True)
    descripcion_carga = models.TextField(blank=True, null=True)
    manifiesto_nro = models.CharField(max_length=255, blank=True, null=True)
    comentarios = models.TextField(blank=True, null=True)
    destinatario = models.ForeignKey(TrackingDestinatarios,on_delete=models.RESTRICT,null=True)
    estado = models.ForeignKey(TrackingEstados,on_delete=models.RESTRICT,null=True)
    manifiesto = models.OneToOneField(Manifiestos,on_delete=models.DO_NOTHING,related_name='tracking')

    class Meta:
        managed = False
        db_table = 'tracking_manifiesto'
        
    def __str__(self):
        return self.manifiesto.serie + '-' + str(self.manifiesto.numero)


class TrackingAdjuntos(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    tracking = models.ForeignKey('TrackingRegistros', models.DO_NOTHING)
    fecha_registro = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tracking_adjuntos'
    
    