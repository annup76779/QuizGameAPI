from django.urls import path

from quizGame.views import home_page, SubjectAreaApis

urlpatterns = [
    path('', home_page, name="index_page"), # default path
    path('subjectarea', SubjectAreaApis.as_view(), name="get_subjectareas")
]