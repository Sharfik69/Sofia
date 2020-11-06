from django.db import models

from authsystem.models import Tag, Candidate, Education, WorkExperience, Company


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
    employer = models.ForeignKey(
        Candidate,
        verbose_name = 'Что за чел',
        null = False,
        on_delete = models.CASCADE
    )