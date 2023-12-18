from django.http import HttpResponse
from django.shortcuts import render

from example.forms import UserForm
from example.models import User


# Create your views here.


def home(request):
    return render(request, 'example/exampleForm.html', context={'form': UserForm()})


def accept(request):
    form = UserForm(request.POST)  # создаём объект формы и заполняем его данными
    if form.is_valid():  # проверяем, что формы содержат все поля(корректность заполнения)
        user = User(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            is_active=form.cleaned_data['is_active']
        )
        user.save()
    else:
        return HttpResponse('Error')
