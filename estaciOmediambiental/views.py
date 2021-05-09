from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.http import JsonResponse
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm

""" from django_app.models import User """


class dades(View):
    def get(self, request):
        pais = request.GET.get('pais')
        ciutat = request.GET.get('ciutat')
        paisFinal = ""
        if pais:
            paisFinal = pais

        ciutatFinal = ""
        if ciutat:
            ciutatFinal = ciutat

        context = {
            'reservas': "reservas",
            'user': "request",
            'pais': paisFinal,
            'map': False,
            'ciutat': ciutatFinal
        }
        return render(request, 'dades.html', context)


class base(View):
    def get(self, request):
        return redirect('/map')


class yourDisplays(View):
    def get(self, request):
        context = {
            'user': request.user.is_authenticated,
            'map': False,
            'reservas': "reservas",
        }
        return render(request, 'yourDisplays.html', context)


class world_map(View):
    def get(self, request):
        pais = request.GET.get('pais')
        paisFinal = ""
        if(pais):
            paisFinal = pais

        context = {
            'map': True,
            'pais': pais
        }
        return render(request, 'world_map.html', context)


class config(View):
    def get(self, request):
        context = {
            'user': request.user.is_authenticated,
            'map': False,
            'reservas': "reservas",
        }
        return render(request, 'config.html', context)


class addDisplay(View):
    def get(self, request):
        context = {
            'user': request.user.is_authenticated,
            'map': False,
            'reservas': "reservas",
        }
        return render(request, 'addDisplay.html', context)


class display(View):
    def get(self, request):
        context = {
            'id': request.GET.get('id'),
            'map': False,
            'reservas': "reservas",
        }
        return render(request, 'display.html', context)


class logIn(View):
    def get(self, request):
        context = {
            'user': request.user.is_authenticated,
            'userID': request.user.username,
            'reservas': "reservas",
        }
        return render(request, 'logIn.html', context=context)

    def post(self, request):

        return redirect('/logIn?err=1')


class logOut(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/dades')


class signIn(View):
    def get(self, request):
        context = {
            'user': request.user.is_authenticated,
            'userID': request.user.username,
            'reservas': "reservas",
        }
        return render(request, 'signIn.html', context=context)
