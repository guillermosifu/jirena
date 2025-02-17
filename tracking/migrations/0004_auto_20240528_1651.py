# Generated by Django 3.2 on 2024-05-28 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20231006_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingAdjuntos',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_registro', models.DateTimeField()),
            ],
            options={
                'db_table': 'tracking_adjuntos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingEstados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tracking_estados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrackingManifiesto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('guia_remision_serie', models.CharField(blank=True, max_length=255, null=True)),
                ('guia_remision_nro', models.BigIntegerField(blank=True, null=True)),
                ('guia_transportista_serie', models.CharField(blank=True, max_length=255, null=True)),
                ('guia_transportista_nro', models.BigIntegerField(blank=True, null=True)),
                ('delivery', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_order', models.CharField(blank=True, max_length=255, null=True)),
                ('orden_compra', models.CharField(blank=True, max_length=255, null=True)),
                ('unidad_minera', models.CharField(blank=True, max_length=255, null=True)),
                ('punto_origen', models.CharField(blank=True, max_length=255, null=True)),
                ('punto_destino', models.CharField(blank=True, max_length=255, null=True)),
                ('peso_total', models.CharField(blank=True, max_length=255, null=True)),
                ('nro_bultos', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_recepcion', models.DateField(blank=True, null=True)),
                ('fecha_inicio_traslado', models.DateField(blank=True, null=True)),
                ('fecha_entrega_programada', models.DateField(blank=True, null=True)),
                ('fecha_entrega_real', models.DateField(blank=True, null=True)),
                ('descripcion_carga', models.TextField(blank=True, null=True)),
                ('manifiesto_nro', models.CharField(blank=True, max_length=255, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tracking_manifiesto',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='trackingdestinatarios',
            options={'managed': False},
        ),
        migrations.AlterField(
            model_name='trackingregistros',
            name='tramo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='tracking', to='tracking.tramos'),
        ),
        migrations.AlterField(
            model_name='trackingregistros',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='tracking.trackingestados'),
        ),
        migrations.DeleteModel(
            name='TrackingEstado',
        ),
    ]
