from django.shortcuts import render

from .models import AboutMe


def about_me(request):
    about_me_data = AboutMe.objects.first()
    return render(request, "main_page/about_me.html", {"about_me": about_me_data})
