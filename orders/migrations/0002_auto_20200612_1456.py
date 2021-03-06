# Generated by Django 2.1.5 on 2020-06-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in U$S', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in U$S', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=10)),
                ('style', models.CharField(choices=[('R', 'Regular'), ('S', 'Sicilian')], max_length=10)),
                ('price', models.IntegerField(help_text='Price in U$S')),
                ('toppings', models.ManyToManyField(to='orders.Topping')),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in U$S', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in U$S', max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='SubExtra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, help_text='Price in U$S', max_digits=4)),
            ],
        ),
        migrations.AddField(
            model_name='sub',
            name='extras',
            field=models.ManyToManyField(blank=True, to='orders.SubExtra'),
        ),
    ]
