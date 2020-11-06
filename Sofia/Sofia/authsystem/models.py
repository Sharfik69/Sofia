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

    def __str__(self):
        return self.name

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
    is_company = models.BooleanField(
        verbose_name='Это компания?',
        default=False
    )
    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'


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


class Company(User):
    name_company = models.CharField(
        max_length=255,
        verbose_name='Название компании'
    )
    FIO_CEO = models.CharField(
        max_length=255,
        verbose_name='ФИО Директора'
    )
    Phone_CEO = models.CharField(
        verbose_name='Телефон Директора',
        max_length=12
    )
    Email_CEO = models.CharField(
        verbose_name='Почта Директора',
        max_length=100
    )
    FIO_Contact = models.CharField(
        max_length=255,
        verbose_name='ФИО Конатктного лица'
    )
    Phone_Contact = models.CharField(
        verbose_name='Телефон Конактного лица',
        max_length=12
    )
    Email_Contact = models.CharField(
        verbose_name='Почта Конатктного лица',
        max_length=12
    )
    description = models.TextField(
        verbose_name='О компании'
    )
    #TODO: Сделать путь куда грущзить лого компании
    img_logo = models.ImageField(upload_to='', blank=True, verbose_name='Логотип компании')
    place = models.CharField(
        verbose_name='Адрес компании',
        max_length=300
    )
    is_company = models.BooleanField(
        verbose_name='Это компания?',
        default=True
    )
    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'


