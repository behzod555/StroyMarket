# Generated by Django 3.2.5 on 2021-08-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210817_1609'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.DeleteModel(
            name='Телефоны',
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('xiaomi', 'Xiaomi'), ('samsung', 'Samsung'), ('apple', 'Apple')], default='xiaomi', max_length=300),
        ),
    ]