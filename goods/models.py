from pyexpat import model
from django.db import models

from utils.choices.choices import RATING_RANGE

class Good(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(max_length=300, verbose_name="Описание")
    photo = models.ImageField(upload_to='goods/%Y/%m/%d', verbose_name="Фото")
    cost = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Цена")
    raiting = models.CharField(
        choices=RATING_RANGE,
        max_length=1,
        default=0,
        verbose_name="Рейтинг"
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.pk)
