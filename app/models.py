﻿"""
Definition of models.
"""

from tabnanny import verbose
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User  # Импортируем модель User

class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date= "posted", verbose_name= "Заголовок")
    description = models.TextField(verbose_name= "Краткое содержание")
    content = models.TextField(verbose_name= "Полное содержание")
    posted = models.DateTimeField(default= datetime.now, db_index= True, verbose_name= "Опубликована")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", default=1)  # Добавляем поле автора on_delete=models.CASCADE - если пользователь удален - его статьи тоже 
    image = models.FileField(default= 'temp.jpg', verbose_name= "Путь к картинке")

    #Методы класса:
    def get_absolute_url(self): #метод возвращает строку с URL-адресом записи
        return reverse("blogpost", args=[str(self.id)])
    def __str__(self):  #метод возвращает название используемое для представления отдельных записей в админ.панеле
        return self.title
    
    #Метаданные - вложенный класс, который задает доп.параметры модели:
    class Meta:
        db_table = "Posts"    #имя таблицы для модели
        ordering = ["-posted"]   #порядок сортировки данных в модели по убыв(-)
        verbose_name = "Статья блога"   #имя, под которым модель будет открываться
        verbose_name_plural = "Статьи блога"   #для всех статей блога

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name= "Текст комментария")
    date = models.DateTimeField(default= datetime.now(),db_index= True, verbose_name= "Дата комментария")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    post = models.ForeignKey(Blog, on_delete= models.CASCADE, verbose_name= "Статья комментария")

    def __str__(self):
        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)

    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = "Комментарий к статье блога"
        verbose_name_plural = "Комментарии к статьям блога"

admin.site.register(Comment)

