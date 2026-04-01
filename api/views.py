from django.http import JsonResponse
from rest_framework.decorators import api_view
from students.models import Students
from . serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view
def studentView(request):
      if(request.method == "GET"):
            students=Students.objects.all()
            serializer=StudentSerializer(students,many=True)
            return Response(serializer.data, status=HTTP_200_OK)
      elif(request.method=="POST"):
                        serializer=StudentSerializer(data=request.data)
                        if(serializer.is_valid()):
                                serializer.save()
                                return Response (serializer.data,status=status.HTTP_201_CREATED)
                        return Response(serializer.errors,status=status.HTTP_404P_BAD_Request)





# 76,209,8014,303,11,