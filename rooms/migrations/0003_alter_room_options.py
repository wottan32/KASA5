# Generated by Django 4.1.4 on 2022-12-08 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20191216_0937'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-pk']},
        ),
    ]
