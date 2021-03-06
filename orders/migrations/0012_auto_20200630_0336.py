# Generated by Django 2.1.5 on 2020-06-30 03:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0011_auto_20200629_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='order',
            name='dinnerplatter',
        ),
        migrations.AddField(
            model_name='order',
            name='dinnerplatter',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.DinnerPlatter'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='pasta',
        ),
        migrations.AddField(
            model_name='order',
            name='pasta',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Pasta'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Pizza'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='order',
            name='salad',
        ),
        migrations.AddField(
            model_name='order',
            name='salad',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Salad'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='order',
            name='sub',
        ),
        migrations.AddField(
            model_name='order',
            name='sub',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.Sub'),
            preserve_default=False,
        ),
    ]
