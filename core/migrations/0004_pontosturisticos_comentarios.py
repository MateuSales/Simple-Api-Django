# Generated by Django 2.2.6 on 2019-10-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
        ('core', '0003_pontosturisticos_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='comentarios',
            field=models.ManyToManyField(to='comentarios.Comentario'),
        ),
    ]
