from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return render(request, "index.html")


def blog(request):
    return HttpResponse("Блог")


def goals(request):
    return HttpResponse("Цели")


def about(request):
    return HttpResponse("Об авторе")


def resources(request):
    return HttpResponse("Материал, который я посчитал полезным")
