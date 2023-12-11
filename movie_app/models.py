from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=15, verbose_name='Режиссер')

    def __str__(self):
        return f'Режиссер: {self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название:')
    description = models.TextField(blank=True, verbose_name='Описание:')
    duration = models.CharField(max_length=10, verbose_name='Продолжительность:')
    director = models.ForeignKey(Director, on_delete=models.Model, verbose_name='Режиссер:')

    def __str__(self):
        return f'Фильмы: {self.title}'

stars = (
    '*', '*',
    '**', '**',
    '***', '***',
    '****', '****',
    '*****', '*****',
)

class Review(models.Model):
    text = models.TextField(max_length=400)
    rate_stars = models.IntegerField(default=1, choices=[(i, i * '*') for i in range(1, 6)])
    movie = models.ForeignKey(Movie, on_delete=models.Model, verbose_name='Обзор', related_name='reviews')

    def __str__(self):
        return f'Обзор: {self.text}'