# Generated by Django 2.2.1 on 2019-07-02 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('king', '0008_auto_20190629_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productpage',
            name='p_desc',
        ),
        migrations.CreateModel(
            name='ProductDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_slides_img1', models.ImageField(default='default/def_slides.jpg', upload_to='product_slides/')),
                ('p_slides_img2', models.ImageField(default='default/def_slides.jpg', upload_to='product_slides/')),
                ('p_slides_img3', models.ImageField(default='default/def_slides.jpg', upload_to='product_slides/')),
                ('p_slides_img4', models.ImageField(default='default/def_slides.jpg', upload_to='product_slides/')),
                ('p_description_short', models.TextField()),
                ('p_img', models.ImageField(default='default/def_slides.jpg', upload_to='product_slides/')),
                ('p_description_long1', models.TextField()),
                ('p_img1', models.ImageField(default='default/def_slides.jpg', upload_to='product_slides/')),
                ('p_description_long2', models.TextField()),
                ('p_title', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='king.ProductPage')),
            ],
        ),
    ]