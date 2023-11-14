from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    male_description = models.CharField(
        max_length=500,
        verbose_name="Маленькое описание"
    )
    image = models.ImageField(
        upload_to='categories/'
    )

    def __str__(self):
        return f"{self.title}"
    
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
