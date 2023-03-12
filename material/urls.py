"""squad2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from material.views import *


urlpatterns = [
    path("", MaterialIndex.as_view(), name="material-index"),
    # path('weapons/', WeaponsList.as_view(), name='weapons'),
    # path('soldiers_card/<pk>/',
    #      SoldiersCard.as_view(), name='soldier-card'),
    # path('ammo/', AmmoList.as_view(), name='ammo'),
]
