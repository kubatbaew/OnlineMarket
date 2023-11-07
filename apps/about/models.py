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


class TeamMember(models.Model):
    image = models.ImageField(
        upload_to="teammembers/",
        verbose_name="Фото",
    )
    full_name = models.CharField(
        max_length=50,
        verbose_name="Полное имя",
    )
    profession = models.CharField(
        max_length=30,
        verbose_name="Профессия",
    )
    
    def __str__(self) -> str:
        return f"{self.full_name}"
    
    
    class Meta:
        verbose_name = "Член Команды"
        verbose_name_plural = "Члены Команды"
