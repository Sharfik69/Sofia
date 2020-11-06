from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

class Candidate(User):
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=12
    )
    addition_contacts = models.TextField(
        verbose_name='Дополнительная контактная информация'
    )
    description = models.TextField(
        verbose_name='О себе'
    )
    tags = models.ManyToManyField(Tag)
    cv = models.FileField(
        verbose_name='Резюме'
    )


class Education(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название учебного заведения'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Название специальности'
    )
    date_finish = models.IntegerField(
        verbose_name='Год окончания'
    )
    user = models.ForeignKey(
        Candidate,
        verbose_name = 'Чье',
        null = False,
        on_delete = models.CASCADE
    )


class WorkExperience(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название компании'
    )
    position = models.CharField(
        max_length=255,
        verbose_name='Название должности'
    )
    description = models.TextField(
        verbose_name='Обязанности'
    )
    date = models.DurationField(
        verbose_name='Период работы'
    )
    user = models.ForeignKey(
        Candidate,
        verbose_name = 'Чье',
        null = False,
        on_delete = models.CASCADE
    )


