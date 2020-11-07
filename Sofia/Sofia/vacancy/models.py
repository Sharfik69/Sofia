from django.db import models

from authsystem.models import Candidate, Education, WorkExperience, Company

class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        primary_key=True
    )
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Vacancy(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    company = models.ForeignKey(
        Company,
        verbose_name = 'Что за компания',
        null = False,
        on_delete = models.CASCADE
    )
    name = models.CharField( 
        max_length=255,
        verbose_name='Название',
        default='НАЗВАНИЕ'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание',
        default='ОПИСАНИЕ'
        
    )
    salary = models.CharField(
        max_length=255,
        verbose_name='Заработная плата',
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name='Теги'
    )
    @classmethod
    def create(cls, company, name, description, salary):
        vacan = cls(company=company, name=name, description=description, salary=salary)
        print(123)
        return vacan
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class users_vacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy,verbose_name = 'Вакансия юзера',
        null = False,
        on_delete = models.CASCADE)
    candidate = models.ForeignKey(Candidate, verbose_name='Какой юзер', null=False, on_delete = models.CASCADE)