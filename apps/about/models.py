from django.db import models


class About(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to='about/',
        verbose_name="Фото",
    )

    def __str__(self):
        return f"{self.title}"
    
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О насы"
