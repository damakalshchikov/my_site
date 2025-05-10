from django.urls import path

from . import views


# От главной страницы идут ссылки на другие страницы
# Блог будте отдельным приложением
# Цели, об авторе, материал, который я посчитал полезным - это отдельные страницы, которые находятся в этом приложении
urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("blog/", views.blog, name="blog"),
    path("goals/", views.goals, name="goals"),
    path("about/", views.about, name="about"),
    path("resources/", views.resources, name="resources"),
]
