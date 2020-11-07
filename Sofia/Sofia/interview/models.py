from django.db import models

from vacancy.models import Vacancy
from authsystem.models import Candidate


class Interview(models.Model):
    # id = models.AutoField(
    #     primary_key=True
    # )
    vacancies = models.ForeignKey(
        Vacancy,
        verbose_name = 'Вакансия',
        null = False,
        on_delete = models.CASCADE
    )
    order = models.IntegerField(
        verbose_name='Порядковый номер этапа'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name + " : " + str(self.id)

    class Meta:
        verbose_name = 'Очное собеседование'
        verbose_name_plural = 'Очные собеседования'

class InterviewQuestion(models.Model):
    # id = models.AutoField(
    #     primary_key=True
    # )
    question = models.CharField(
        verbose_name='Вопрос',
        max_length=255
    )
    interview = models.ForeignKey(
        Interview,
        verbose_name='Интервью',
        null = False,
        on_delete = models.CASCADE
    )
    order = models.IntegerField(
        verbose_name='Номер вопроса'
    )
    def __str__(self):
        return self.question + " : " + self.id
        
    class Meta:
        verbose_name = 'Вопрос собеседования'
        verbose_name_plural = 'Вопросы собеседования'

class InterviewTags(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    text = models.CharField(
        max_length=255,
        verbose_name='тэг для быстрого ответа'
    )
    question = models.ForeignKey(
        InterviewQuestion,
        verbose_name='Вопрос тэга',
        null = False,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Тэг вопроса собеседования'
        verbose_name_plural = 'Теги'

class InterviewAnswer(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    question = models.ForeignKey(
        InterviewQuestion,
        verbose_name='Вопрос тэга',
        null = False,
        on_delete = models.CASCADE
    )
    respondent = models.ForeignKey(
        Candidate,
        verbose_name='Соискатель',
        null = False,
        on_delete = models.CASCADE
    )
    answer = models.TextField(
        verbose_name='Результат'
    )
    def __str__(self):
        return 'Соискатель: {0}. Вопрос: {1}. Ответ: {2}'.format(self.respondent, self.question, self.answer)
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'