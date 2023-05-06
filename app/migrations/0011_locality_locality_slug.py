# Generated by Django 4.1.4 on 2023-04-24 14:50

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_locality'),
    ]

    operations = [
        migrations.AddField(
            model_name='locality',
            name='locality_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]