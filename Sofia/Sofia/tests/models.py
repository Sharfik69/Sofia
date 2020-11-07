from django.db import models
from vacancy.models import Vacancy
from authsystem.models import Candidate


class Test(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    vacancy = models.ForeignKey(
        Vacancy,
        verbose_name='Вакансия',
        null=False,
        on_delete=models.CASCADE
    )
    order = models.IntegerField(
        verbose_name='Порядок',
    )


class TestQuestion(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    id_test = models.ForeignKey(
        Test,
        verbose_name='Тест',
        null=False,
        on_delete=models.CASCADE
    )
    quest = models.TextField(
        verbose_name='Вопрос',
    )
    type = models.IntegerField(
        verbose_name='Тип вопроса',  # 0 - Один ответ; 1 - несколько ответов; 2 - открытый ответ (одно слово)
        default=0,
    )
    jsn_ans = models.TextField(
        verbose_name='Варианты ответа',
    )
    jsn_is_true = models.TextField(
        verbose_name='Какие варианты ответа верны?',
    )


class ResultsTest(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    candidate = models.ForeignKey(
        Candidate,
        verbose_name='Соискатель',
        null=False,
        on_delete=models.CASCADE
    )
    id_test = models.ForeignKey(
        Test,
        verbose_name='Тест',
        null=False,
        on_delete=models.CASCADE
    )
    vacancy = models.ForeignKey(
        Vacancy,
        verbose_name='Вакансия',
        null=False,
        on_delete=models.CASCADE
    )
    ans = models.TextField(
        verbose_name='Ответы пользователя'
    )
    accuracy = models.IntegerField(
        verbose_name='Процент верных ответов'
    )
    order = models.IntegerField(
        verbose_name='порядок'
    )


