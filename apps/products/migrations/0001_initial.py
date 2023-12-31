# Generated by Django 4.2.6 on 2023-11-10 09:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0003_category_level_category_lft_category_rght_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123, verbose_name='Название')),
                ('description', ckeditor.fields.RichTextField(max_length=1000, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('size', models.CharField(choices=[('S', 'S'), ('L', 'L'), ('M', 'M'), ('XL', 'XL')], max_length=2, verbose_name='Размер')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category', verbose_name='Категория')),
                ('images', models.ManyToManyField(blank=True, to='products.image', verbose_name='Изображения')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
