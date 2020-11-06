# Generated by Django 3.1.3 on 2020-11-06 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quest', models.TextField(verbose_name='Вопрос')),
                ('type', models.IntegerField(verbose_name='Тип вопроса')),
                ('jsn_ans', models.TextField(verbose_name='Варианты ответа')),
                ('jsn_is_true', models.TextField(verbose_name='Какие варианты ответа верны?')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.IntegerField(verbose_name='Порядок')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.testquestion', verbose_name='Вопросы')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.vacancy', verbose_name='Вакансия')),
            ],
        ),
    ]
