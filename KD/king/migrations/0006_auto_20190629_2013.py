# Generated by Django 2.2.1 on 2019-06-29 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('king', '0005_auto_20190629_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='p_img',
            field=models.ImageField(default='default/def.png', upload_to='product_samples/%Y/%m/%d/'),
        ),
    ]
