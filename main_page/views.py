from django.http import HttpResponse


def about_me(request):
    return HttpResponse("Hello, World!")
