from django.urls import path

from apps.about.views import about_page


urlpatterns = [
    path('about/', about_page, name="about"),
]
