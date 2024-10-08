# Generated by Django 4.2.16 on 2024-09-13 19:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Triaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_triaje', models.DateTimeField(auto_now_add=True)),
                ('frecuencia_cardiaca', models.IntegerField(help_text='Frecuencia cardíaca en latidos por minuto (60-100)', validators=[django.core.validators.MinValueValidator(60), django.core.validators.MaxValueValidator(100)])),
                ('frecuencia_respiratoria', models.IntegerField(help_text='Frecuencia respiratoria en respiraciones por minuto (12-20)', validators=[django.core.validators.MinValueValidator(12), django.core.validators.MaxValueValidator(20)])),
                ('presion_arterial_min', models.IntegerField(help_text='Presión arterial mínima (80-84 mmHg)', validators=[django.core.validators.MinValueValidator(80), django.core.validators.MaxValueValidator(84)])),
                ('presion_arterial_max', models.IntegerField(help_text='Presión arterial máxima (120-129 mmHg)', validators=[django.core.validators.MinValueValidator(120), django.core.validators.MaxValueValidator(129)])),
                ('temperatura_corporal', models.DecimalField(decimal_places=1, help_text='Temperatura corporal en grados centígrados (12.0-40.0)', max_digits=4, validators=[django.core.validators.MinValueValidator(12.0), django.core.validators.MaxValueValidator(40.0)])),
                ('spo2', models.DecimalField(decimal_places=1, help_text='Nivel de saturación de oxígeno en porcentaje (70.0-100.0)', max_digits=4, validators=[django.core.validators.MinValueValidator(70.0), django.core.validators.MaxValueValidator(100.0)])),
                ('prioridad', models.CharField(choices=[('BAJA', 'Baja'), ('MEDIA', 'Media'), ('ALTA', 'Alta')], default='BAJA', max_length=50)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='triajes', to='paciente.paciente')),
            ],
            options={
                'verbose_name_plural': 'Triajes',
            },
        ),
    ]
