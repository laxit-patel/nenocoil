# Generated by Django 2.1.4 on 2019-03-28 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190328_0918'),
        ('reservoir', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductType',
        ),
    ]
