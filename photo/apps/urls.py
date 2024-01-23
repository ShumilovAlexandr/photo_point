from django.urls import path

from . import views

urlpatterns = [
    path("get-current-usd/", views.get_current_course, name="main_page"),
]
