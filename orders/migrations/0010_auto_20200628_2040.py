# Generated by Django 2.1.5 on 2020-06-28 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_cart_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dinnerplatter_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='pasta_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='pizza_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='salad_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
