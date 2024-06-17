from .models import User
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django import forms


class UserForm(ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['mail', 'login', 'password1', 'password2']
        # widgets = {
        #     "mail": EmailInput(attrs={
        #         'class': 'form_group',
        #         'placeholder': 'Введите почту'
        #     }),
        #     "login": TextInput(attrs={
        #         'class': 'form_group',
        #         'placeholder': 'Введите логин'
        #     }),
        #     "password": PasswordInput(attrs={
        #         'class': 'form_group',
        #         'placeholder': 'Введите пароль'
        #     })
        # }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
