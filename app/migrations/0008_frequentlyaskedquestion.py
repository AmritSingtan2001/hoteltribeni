# Generated by Django 4.1.4 on 2023-04-24 10:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_packages_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequentlyAskedQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('discriptions', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'ordering': ['id'],
            },
        ),
    ]
