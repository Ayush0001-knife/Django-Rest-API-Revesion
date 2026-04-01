from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.status import HTTP_200_OK
from . models import Students
from api.serializers import StudentSerializer
from rest_framework.status import HTTP_200_OK



# Create your views here.
def students(request):
      students = Students.objects.all()
      serializer=StudentSerializer(students,many=True)
      return JsonResponse(serializer.data, status=HTTP_200_OK)