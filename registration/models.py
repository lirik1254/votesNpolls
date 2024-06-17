from django.db import models


class User(models.Model):
    mail = models.EmailField('Почта')
    login = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return f'Логин: {self.login}'
