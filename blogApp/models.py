from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    image = models.CharField("Ссылка на изображение", max_length=500)
    description = models.TextField("Описание")
    post_date = models.DateTimeField("Дата публикаций", default=datetime.now)

class Meta:
    verbose_name = "Пост"
    verbose_name_plural = "Новости"

    def __str__(self):
        return self.title