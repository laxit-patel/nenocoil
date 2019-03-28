# Generated by Django 2.1.4 on 2019-03-28 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_Id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Order_Amount', models.CharField(max_length=10)),
                ('Order_Date', models.DateTimeField()),
                ('Order_Deadline', models.DateTimeField()),
                ('Order_Reference', models.CharField(max_length=128)),
                ('Order_Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
                ('Order_Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
