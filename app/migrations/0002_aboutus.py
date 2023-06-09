# Generated by Django 4.1.4 on 2023-04-23 15:17

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discriptions', ckeditor.fields.RichTextField()),
                ('image1', models.ImageField(upload_to='aboutimage/')),
                ('image2', models.ImageField(upload_to='aboutimage/')),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
