from django.db import models

# Create your models here.


class Aerolinea(models.Model):
    id_aerolinea = models.AutoField(primary_key=True)
    nombreaerolinea = models.CharField(db_column='nombreAerolinea', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aerolinea'


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombrecategoria = models.CharField(db_column='nombreCategoria', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorias'


class Destinos(models.Model):
    id_destino = models.AutoField(primary_key=True)
    nombredestino = models.CharField(db_column='nombreDestino', max_length=100)  # Field name made lowercase.
    preciodestino = models.IntegerField(db_column='precioDestino')  # Field name made lowercase.
    fecha_salida = models.DateTimeField(blank=True, null=True)
    cantidaddisponible = models.IntegerField(db_column='cantidadDisponible')  # Field name made lowercase.
    id_aerolinea = models.ForeignKey(Aerolinea, models.DO_NOTHING, db_column='id_aerolinea')
    id_metodopago = models.ForeignKey('MetodoPago', models.DO_NOTHING, db_column='id_metodoPago')  # Field name made lowercase.
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'destinos'


class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    nombrelocalidad = models.CharField(db_column='nombreLocalidad', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localidad'


class MetodoPago(models.Model):
    id_metodopago = models.AutoField(db_column='id_metodoPago', primary_key=True)  # Field name made lowercase.
    nombrepago = models.CharField(db_column='nombrePago', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class ObraSocial(models.Model):
    id_obrasocial = models.AutoField(db_column='id_obraSocial', primary_key=True)  # Field name made lowercase.
    nombreobrasocial = models.CharField(db_column='nombreObraSocial', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'obra_social'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    passw = models.CharField(max_length=100)
    direccion = models.CharField(max_length=300)
    dni = models.IntegerField()
    telefono = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    id_localidad = models.ForeignKey(Localidad, models.DO_NOTHING, db_column='id_localidad')
    id_metodopago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='id_metodoPago')  # Field name made lowercase.
    id_obrasocial = models.ForeignKey(ObraSocial, models.DO_NOTHING, db_column='id_obraSocial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuario'
