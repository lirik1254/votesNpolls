from django.forms import inlineformset_factory, modelformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect
from registration.models import User
from .models import Poll, Choice
from .forms import *


def profile(request):
    return render(request, "user/profile.html")


def voting(request):
    ChoiceFormSet = modelformset_factory(Choice, form=ChoiceForm, extra=4)
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        formset = ChoiceFormSet(request.POST, queryset=Choice.objects.none())
        if poll_form.is_valid() and formset.is_valid():
            poll = poll_form.save(commit=False)
            user_id = request.session.get('user_id')
            user = User.objects.get(id=user_id)
            poll.creator = user
            poll.save()
            for form in formset.cleaned_data:
                if form:
                    choice = form['text']
                    Choice(poll=poll, text=choice).save()
            return render(request, 'user/profile.html', {'user': user})
    else:
        poll_form = PollForm()
        formset = ChoiceFormSet(queryset=Choice.objects.none())
    return render(request, 'user/create.html', {'poll_form': poll_form, 'formset': formset})


def getUserVotingChoices(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            user_polls = user.created_polls.all()
            poll_choices = []
            for poll in user_polls:
                choices = poll.choices.all()
                poll_choices.append((poll, choices))

            context = {
                'user': user,
                'user_polls': user_polls,
                'poll_choices': poll_choices
            }
            return render(request, 'user/voting.html', context)
        except User.DoesNotExist:
            # В случае ошибки (пользователь удален или не существует)
            return HttpResponse('Ошибка: Пользователь не найден.')
    else:
        # Если user_id не установлен в сессии (пользователь не аутентифицирован)
        return redirect('login')  # Перенаправление на страницу входа или другую страницу


def empty(request):
    return render(request, "user/empty_page.html")
# def voting(request):
#     ChoiceFormSet = inlineformset_factory(Poll, Choice, form=ChoiceForm, extra=1, can_delete=True)
#
#     if request.method == 'POST':
#         poll_form = PollForm(request.POST)
#         choice_formset = ChoiceFormSet(request.POST)
#
#         if poll_form.is_valid() and choice_formset.is_valid():
#             poll = poll_form.save(commit=False)
#             user_id = request.session.get('user_id')
#             user = User.objects.get(id=user_id)
#             poll.creator = user
#             poll.save()
#
#             choice_formset.instance = poll
#             choice_formset.save()
#
#             return redirect('profile')
#         else:
#             print("Poll Form Errors:", poll_form.errors)
#             print("Choice Formset Errors:", choice_formset.errors)
#     else:
#         poll_form = PollForm()
#         choice_formset = ChoiceFormSet()
#
#     context = {
#         'poll_form': poll_form,
#         'choice_formset': choice_formset,
#     }
#     return render(request, 'user/create.html', context)
