from django.urls import path

from quizGame.views import home_page

urlpatterns = [
    path('', home_page, name="index_page"), # default path
]