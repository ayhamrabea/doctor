# Generated by Django 4.2.2 on 2023-06-16 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_service_descreption_alter_service_image'),
        ('appoitment', '0006_remove_appoitment_doctor_remove_appoitment_server_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoitment',
            name='server',
        ),
        migrations.AddField(
            model_name='appoitment',
            name='server',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.service', verbose_name='service'),
        ),
    ]
