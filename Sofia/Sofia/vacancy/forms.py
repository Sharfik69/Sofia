from django import forms

class vacancy_form(forms.Form):
    name = forms.CharField(label='Должность', max_length=30)
    description = forms.CharField(label='Описание вакансии', widget=forms.Textarea)
    salary = forms.CharField(label='Зарплата', max_length=30)