from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SubjectArea


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


# region APIs

class SubjectAreaApis(APIView):
    def get(self, request):
        subjectAreas = SubjectArea.objects.all()  # select * from quizGame_subjectarea;
        return Response([
            {"id": data.id, "name": data.name}
            for data in subjectAreas
        ])

# endregion
