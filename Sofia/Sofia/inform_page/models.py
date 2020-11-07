from django.db import models
from vacancy.models import Vacancy
class Text(models.Model):
    html_text = models.TextField(
        verbose_name='Текст для пользователя с картинками'
    )
    vacancy_id = models.ForeignKey(Vacancy, 
        verbose_name = 'Какая вакансия',
        null = False,
        on_delete = models.CASCADE)
    stage = models.IntegerField(verbose_name='Номер стадии', default=1)

    def get_text(self):
        return self.html_text

    @classmethod
    def create(cls, text, vacancy):
        new_text = cls(html_text=text, vacancy_id=vacancy)
        return new_text