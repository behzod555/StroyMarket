# Generated by Django 3.2.5 on 2021-08-17 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('store', '0007_refrigirator'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Telefon',
        ),
        migrations.RenameModel(
            old_name='Refrigirator',
            new_name='TV',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='telefon',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='tv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.tv'),
        ),
    ]