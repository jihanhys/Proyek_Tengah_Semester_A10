# Generated by Django 4.1.1 on 2022-11-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproduct', '0003_remove_product_idtoko_alter_product_toko'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='toko',
        ),
        migrations.AddField(
            model_name='product',
            name='id_toko',
            field=models.IntegerField(default=0),
        ),
    ]