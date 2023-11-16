from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=15, verbose_name='Режиссер')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.data = None

    def __str__(self):
        return f'Режиссер: {self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название:')
    description = models.TextField(blank=True, verbose_name='Описание:')
    duration = models.CharField(max_length=10, verbose_name='Продолжительность:')
    director = models.ForeignKey(Director, on_delete=models.Model, verbose_name='Режиссер:')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.data = None

    def __str__(self):
        return f'Фильмы: {self.title}'


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.Model, verbose_name='Обзор')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.data = None

    def __str__(self):
        return f'Обзор: {self.text}'