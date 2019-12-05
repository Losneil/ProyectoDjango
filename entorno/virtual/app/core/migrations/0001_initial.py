# Generated by Django 2.2 on 2019-11-13 15:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Correo electronico')),
                ('tipom', models.CharField(choices=[('Petición', 'Petición'), ('Solicitud', 'Solicitud'), ('Queja', 'Queja'), ('Reclamo', 'Reclamo'), ('Felicitación', 'Felicitación')], default='Petición', max_length=50, verbose_name='Categoria')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('mensaje', ckeditor.fields.RichTextField(default='Quisiera', verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Mensajes PQRSF',
                'verbose_name_plural': 'Mensajes PQRSF',
            },
        ),
    ]