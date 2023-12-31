from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Message(models.Model):
    text = models.TextField(verbose_name='текст')
    author = models.CharField(max_length=200, verbose_name='автор', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='опубликовано')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
