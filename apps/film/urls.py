from django.urls import path
from apps.film.views import FilmView


urlpatterns = [
    path('', FilmView.as_view(), name='home')
]