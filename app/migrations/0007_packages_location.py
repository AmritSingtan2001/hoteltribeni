# Generated by Django 4.1.4 on 2023-04-24 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='location',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
