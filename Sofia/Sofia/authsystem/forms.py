from django import forms

class Company_new_form(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=30)
    password1 = forms.CharField(label = 'Пароль', widget=forms.TextInput(attrs={'type': 'password'}))
    password2 = forms.CharField(label = 'Повторите пароль', widget=forms.TextInput(attrs={'type': 'password'}))
    name_company = forms.CharField(label='Наименование компании', max_length=30)
    FIO_CEO = forms.CharField(label='ФИО директора', max_length=70)
    Phone_CEO = forms.CharField(label = 'Телефон директора', widget=forms.TextInput(attrs={'type': 'tel'}))
    Email_CEO = forms.CharField(label = 'Почта директора', widget=forms.TextInput(attrs={'type': 'email'}))
    FIO_Contact = forms.CharField(label='ФИО контактного лица', max_length=70)
    Phone_Contact = forms.CharField(label = 'Телефон конактного лица', widget=forms.TextInput(attrs={'type': 'tel'}))
    Email_Contact = forms.CharField(label = 'Почта контактного лица', widget=forms.TextInput(attrs={'type': 'email'}))
    description = forms.CharField(label = 'О компании', widget=forms.Textarea)
    img_logo = forms.FileField()
    place = forms.CharField(label='Адрес компании', max_length=500)


class Employer_new_form(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=30)
    password1 = forms.CharField(label = 'Пароль', widget=forms.TextInput(attrs={'type': 'password'}))
    password2 = forms.CharField(label = 'Повторите пароль', widget=forms.TextInput(attrs={'type': 'password'}))
    phone = forms.CharField(label = 'Телефон', widget=forms.TextInput(attrs={'type': 'tel'}))
    addition_contacts = forms.CharField(label = 'Дополнительная контактная информация', widget=forms.Textarea)
    description = forms.CharField(label = 'Дополнительная информация о себе', widget=forms.Textarea)
    cv = forms.FileField()