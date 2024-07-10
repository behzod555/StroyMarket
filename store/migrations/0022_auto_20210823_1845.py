# Generated by Django 3.2.5 on 2021-08-23 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('store', '0021_auto_20210821_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('бытовые-техники', 'Бытовые-техники'), ('компьютерная-техника', 'Компьютерная-техника'), ('климатическая-техника', 'Климатическая-техника'), ('спортивные-товары', 'Спортивные-товары'), ('мужские-туфли', 'Мужские-туфли'), ('телефоны', 'Телефоны'), ('телевизоры', 'Телевизоры')], max_length=300),
        ),
        migrations.AlterField(
            model_name='televizory',
            name='category',
            field=models.CharField(choices=[('samsung', 'Samsung'), ('lg', 'Lg'), ('sony', 'Sony')], max_length=300),
        ),
    ]