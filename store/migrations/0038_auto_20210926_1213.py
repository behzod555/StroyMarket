# Generated by Django 3.2.5 on 2021-09-26 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('store', '0037_phones'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage', models.CharField(max_length=300, verbose_name='Название продукта')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product', verbose_name='Название товара')),
            ],
        ),
        migrations.DeleteModel(
            name='Phones',
        ),
    ]