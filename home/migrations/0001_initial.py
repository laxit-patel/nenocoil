# Generated by Django 2.1.4 on 2018-12-10 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('Client_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Client_name', models.CharField(max_length=50)),
                ('Client_gstin', models.CharField(max_length=20)),
                ('Client_address', models.TextField(max_length=500)),
                ('Client_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('Invoice_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Invoice_number', models.CharField(max_length=10)),
                ('Invoice_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Client')),
            ],
        ),
    ]
