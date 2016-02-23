# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    bash_id = models.PositiveIntegerField(u'bash.im id')
    added_date = models.DateTimeField(u'Дата загрузки', auto_now_add=True)
    text = models.TextField(u'Контент')

    class Meta:
        verbose_name = u'Сообщение'
        verbose_name_plural = u'Сообщения'
