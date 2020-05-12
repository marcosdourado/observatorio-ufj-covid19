# Generated by Django 3.0.6 on 2020-05-07 20:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoletimEpidemiologico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=256, verbose_name='Cidade')),
                ('data_atualizacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de atualização')),
                ('fonte_oficial', models.URLField(verbose_name='Fonte Oficial (URL)')),
                ('confirmados', models.PositiveIntegerField(null=True, verbose_name='Confirmados')),
                ('recupados', models.PositiveIntegerField(null=True, verbose_name='Recuperados')),
                ('obitos', models.PositiveIntegerField(null=True, verbose_name='Óbitos')),
                ('suspeitos', models.PositiveIntegerField(null=True, verbose_name='Suspeitos')),
                ('investigados', models.PositiveIntegerField(null=True, verbose_name='Investigados/Análise Laboratorial')),
                ('descartados', models.PositiveIntegerField(null=True, verbose_name='Descartados/Excluídos/Negativos')),
                ('monitorados', models.PositiveIntegerField(null=True, verbose_name='Monitorados')),
                ('notificados', models.PositiveIntegerField(null=True, verbose_name='Notificados')),
                ('isolados', models.PositiveIntegerField(null=True, verbose_name='Isolados')),
                ('internados', models.PositiveIntegerField(null=True, verbose_name='Internados')),
                ('enfermaria', models.PositiveIntegerField(null=True, verbose_name='Enfermaria')),
                ('uti', models.PositiveIntegerField(null=True, verbose_name='UTI')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Uuid')),
            ],
            options={
                'verbose_name': 'Boletim',
                'verbose_name_plural': 'Boletins',
                'unique_together': {('cidade', 'data_atualizacao')},
            },
        ),
    ]