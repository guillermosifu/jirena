# Generated by Django 3.2 on 2024-04-25 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('catalogo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='viajes.catalogo')),
            ],
        ),
    ]
