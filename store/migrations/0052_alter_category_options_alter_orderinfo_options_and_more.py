# Generated by Django 4.0.3 on 2022-03-23 01:07

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('store', '0051_order_paid_alter_order_complete_orderinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('ordering',), 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': 'Информации о заказе', 'verbose_name_plural': 'Информации о заказе'},
        ),
        migrations.AddField(
            model_name='order',
            name='order_key',
            field=models.CharField(default=1, max_length=25, verbose_name='Имя:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]