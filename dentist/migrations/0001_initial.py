# Generated by Django 4.2.2 on 2023-06-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='doctors')),
                ('specialist', models.CharField(choices=[('General Dentist', 'General Dentist'), ('Pedodontist ', 'Pedodontist '), ('Orthodontist.', 'Orthodontist.'), ('Periodontist ', 'Periodontist '), ('Endodontist ', 'Endodontist '), ('Oral Pathologist ', 'Oral Pathologist ')], max_length=60)),
                ('experiencce', models.IntegerField()),
                ('about_me', models.TextField(max_length=250)),
                ('add_at', models.DateField(auto_now_add=True)),
                ('facebook', models.URLField()),
                ('instgram', models.URLField()),
                ('linkedin', models.URLField()),
                ('twitter', models.URLField()),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctors',
            },
        ),
    ]