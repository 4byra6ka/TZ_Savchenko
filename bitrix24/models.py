from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Bitrix24(models.Model):
    full_name = models.CharField(max_length=256, verbose_name='Фамилия Имя Отчество')
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Cоздание сделки'
        verbose_name_plural = 'Cоздание сделки'
