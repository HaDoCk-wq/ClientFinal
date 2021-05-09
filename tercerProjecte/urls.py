"""tercerProjecte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

######## Views #########
from estaciOmediambiental.views import dades, yourDisplays, world_map, config, addDisplay, display, logIn, signIn, base


urlpatterns = [
    path('', include('pwa.urls')),

    ##### Views ######
    path('', base.as_view()),

    path('data', dades.as_view()),
    path('yourDisplays', yourDisplays.as_view()),
    path('map', world_map.as_view()),
    path('config', config.as_view()),
    path('addDisplay', addDisplay.as_view()),
    path('display', display.as_view()),
    path('logIn', logIn.as_view()),
    path('signIn', signIn.as_view())

]
