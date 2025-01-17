# Generated by Django 3.2.5 on 2021-10-14 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('store', '0039_delete_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('ordering', models.IntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('ordering',),
            },
        ),
        migrations.DeleteModel(
            name='Catalog',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category'),
        ),
    ]