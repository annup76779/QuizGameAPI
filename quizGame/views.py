from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SubjectArea
from rest_framework import status


# Create your views here.
def home_page(request):
    return render(request, 'home.html')


# region APIs

class SubjectAreaApis(APIView):
    def get(self, request):
        subjectAreas = SubjectArea.objects.order_by("-id").all()  # select * from quizGame_subjectarea;
        return Response([
            {"id": data.id, "name": data.name}
            for data in subjectAreas
        ])

    def post(self, request):
        # name = request.POST.get('name')  # - Used FormData
        name = request.data.get('name')    # - Used Raw Data

        try:
            new_subject_area = SubjectArea(name=name)
            new_subject_area.save()
            return Response({
                "id": new_subject_area.id,
                "name": new_subject_area.name
            })
        except IntegrityError as error:
            return Response({
                "error": f"Subject area `{name}` already exists!"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as error:
            return Response({
                "error": "Unexpected error occurred!"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        subject_area_id = request.data.get("id")
        subject_area_name = request.data.get("name")

        try:
            # get subject area with id
            subject_area = SubjectArea.objects.get(id=subject_area_id)

            # Set new subject area name in the name field of fetched subject area
            subject_area.name = subject_area_name

            try:
                # now try to save updated subject area into database
                # if there is any subject area already with the new given name, you will get IntegrityError
                subject_area.save()
            except IntegrityError:
                return Response({
                    "error": f"Subject area `{subject_area_name}` already exists!"
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({
                "id": subject_area.id,
                "name": subject_area.name
            })
        except SubjectArea.DoesNotExist:
            return Response({
                "error": f"Subject area with id=`{subject_area_id} does not exist!"
            }, status=status.HTTP_404_NOT_FOUND)


# endregion
