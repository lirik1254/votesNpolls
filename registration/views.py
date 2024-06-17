from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import UserForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from .models import User


def authorisation(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            error_message = ""
            try:
                user = User.objects.get(login=login)
                if password == user.password:
                    # Если пароль совпадает, выполните вход пользователя
                    # Можно также использовать authenticate() и login() Django
                    # authenticate(request, username=login, password=password)
                    # login(request, user)
                    # Вместо этого примера

                    request.session['user_id'] = user.id  # Пример использования сеанса
                    return render(request, 'user/profile.html', {'user': user})
                else:
                    error_message = "Неправильный логин/почта или пароль."
            except User.DoesNotExist:
                error_message = "Пользователь с таким логином/почтой не найден."

            if error_message != "":
                try:
                    user = User.objects.get(mail=login)
                    if password == user.password:
                        # Если пароль совпадает, выполните вход пользователя
                        # Можно также использовать authenticate() и login() Django
                        # authenticate(request, username=login, password=password)
                        # login(request, user)
                        # Вместо этого примера

                        request.session['user_id'] = user.id  # Пример использования сеанса
                        return render(request, 'user/profile.html', {'user': user})
                    else:
                        error_message = "Неправильный логин/почта или пароль."
                except User.DoesNotExist:
                    error_message = "Пользователь с таким логином/почтой не найден."

            # Если вход не выполнен, показываем форму с сообщением об ошибке
            return render(request, 'registration/authorisation.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'registration/authorisation.html', {'form': form})


def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            mail = form.cleaned_data['mail']

            try:
                user = User.objects.get(mail=mail)
                messages.error(request, 'Пользователь с такой почтой уже существует!')
            except User.DoesNotExist:
                pass

            try:
                user = User.objects.get(login=login)
                messages.error(request, 'Пользователь с таким логином уже существует!')
            except User.DoesNotExist:
                pass

            if not messages.get_messages(request):
                form.save()
                messages.success(request, 'Вы успешно зарегистрировались!')
                return redirect('authorisation')
        else:
            messages.error(request, 'Пароли не совпадают!')
    else:
        form = UserForm()

    return render(request, 'registration/registration.html', {'form': form})


def succes(request):
    return render(request, "registration/succes.html")
