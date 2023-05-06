# Generated by Django 4.1.4 on 2023-04-24 14:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_frequentlyaskedquestion_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='localityimage/')),
                ('location', models.CharField(max_length=150)),
                ('discriptions', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Locality',
                'verbose_name_plural': 'Localities',
                'ordering': ['-id'],
            },
        ),
    ]
