# Generated by Django 4.2.2 on 2023-06-16 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_service_descreption_alter_service_image'),
        ('dentist', '0002_rename_instgram_doctor_instagram'),
        ('appoitment', '0005_alter_appoitment_appoitment_data_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appoitment',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='appoitment',
            name='server',
        ),
        migrations.AddField(
            model_name='appoitment',
            name='doctor',
            field=models.ManyToManyField(to='dentist.doctor', verbose_name='doctor'),
        ),
        migrations.AddField(
            model_name='appoitment',
            name='server',
            field=models.ManyToManyField(to='service.service', verbose_name='service'),
        ),
    ]