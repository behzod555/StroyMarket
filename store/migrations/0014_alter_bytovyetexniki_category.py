# Generated by Django 3.2.5 on 2021-08-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    
    dependencies = [
        ('store', '0013_alter_bytovyetexniki_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bytovyetexniki',
            name='category',
            field=models.CharField(choices=[('pylesosy', 'Пылесосы'), ('stiralki', 'Стиральные машины'), ('xolodilniki', 'Холодильники')], default='xiaomi', max_length=300),
        ),
    ]