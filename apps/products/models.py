from django.db import models
from ckeditor.fields import RichTextField

from apps.categories.models import Category


class Image(models.Model):
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Картинка",
    )
    
    def __str__(self):
        return self.image.path


class Product(models.Model):
    SIZE_CHOICES = [
        ("S", "S"),
        ("L", "L"),
        ("M", "M"),
        ("XL", "XL"),
    ]
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    
    title = models.CharField(
        max_length=123,
        verbose_name="Название",
    )
    description = RichTextField(
        max_length=1000,
        verbose_name="Описание",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    size = models.CharField(
        verbose_name="Размер",
        choices=SIZE_CHOICES,
        max_length=2,
    )
    images = models.ManyToManyField(
        Image,
        blank=True,
        verbose_name="Изображения",
    )
    
    def __str__(self):
        return f"{self.title}"
    
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
    