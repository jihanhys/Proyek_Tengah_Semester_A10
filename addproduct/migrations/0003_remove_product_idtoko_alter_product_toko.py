# Generated by Django 4.1.1 on 2022-11-01 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addproduct', '0002_product_idtoko'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='idToko',
        ),
        migrations.AlterField(
            model_name='product',
            name='toko',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]