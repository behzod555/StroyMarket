# Generated by Django 3.2.5 on 2021-08-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210817_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('xiaomi', 'Xiaomi'), ('samsung', 'Samsung'), ('apple', 'Apple')], default='xiaomi', max_length=300)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='tv',
            name='category',
            field=models.CharField(choices=[('samsung', 'Samsung'), ('lg', 'Lg'), ('sony', 'Sony')], default='xiaomi', max_length=300),
        ),
    ]
