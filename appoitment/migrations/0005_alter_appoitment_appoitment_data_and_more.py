# Generated by Django 4.2.2 on 2023-06-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appoitment', '0004_alter_appoitment_appoitment_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoitment',
            name='appoitment_data',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appoitment',
            name='appoitment_time',
            field=models.TimeField(),
        ),
    ]
