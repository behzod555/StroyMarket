# Generated by Django 3.2.5 on 2021-08-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('store', '0012_alter_bytovyetexniki_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bytovyetexniki',
            name='category',
            field=models.CharField(choices=[('0', 'Пылесосы'), ('1', 'Стиральные машины'), ('2', 'Холодильники')], default='xiaomi', max_length=300),
        ),
    ]