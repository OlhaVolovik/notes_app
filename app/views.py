from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from app.models import Category, Notation
from app.forms import NotationForm, RegistrationForm, CustomAuthenticationForm


def index(request):
    categories = {category: Notation.objects.filter(category=category) for category in Category.objects.all()}
    return render(request, 'app/main.html', {'categories': categories})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return HttpResponseRedirect('/notes/index')
    return render(request, 'registration/login.html', {'form': CustomAuthenticationForm()})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return HttpResponseRedirect('/notes/index')


def register(request):
    if request.method == 'POST':
        new_user = RegistrationForm(request.POST)

        if new_user.is_valid():
            new_user.save()
            return HttpResponseRedirect('/notes/index')
    return render(request, 'registration/registration.html', {'form': RegistrationForm()})


def create_notation(request):
    if request.method == 'POST':
        new_notation_form = NotationForm(request.POST)

        if new_notation_form.is_valid():
            new_notation_form.save()
            return HttpResponseRedirect('/notes/index')
    else:
        new_notation_form = NotationForm()

    return render(request, 'app/create_notation.html', {'form': new_notation_form})


def delete_notation(request, id):
    notation = Notation.objects.get(id=id)
    notation.delete()
    return HttpResponseRedirect('/notes/index')


def update_notation(request, id):
    notation = Notation.objects.get(id=id)
    categories = Category.objects.all()

    if request.method == 'POST':
        notation.title = request.POST.get('title', False)
        notation.text = request.POST.get('text', False)
        notation.reminder = request.POST.get('reminder', False)

        category = Category.objects.get(slug=request.POST.get('category', False))
        notation.category = category
        notation.save()
        return HttpResponseRedirect('/notes/index')

    return render(request, 'app/update_notation.html', {
        'notation': notation,
        'categories': categories
    })
