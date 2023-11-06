from django.db import models


class Category(models.Model):
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
