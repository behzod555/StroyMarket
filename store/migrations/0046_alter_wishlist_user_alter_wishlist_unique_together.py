# Generated by Django 4.0.2 on 2022-02-24 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0045_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together={('user', 'product')},
        ),
    ]