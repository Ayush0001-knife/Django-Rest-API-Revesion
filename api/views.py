from django.http import JsonResponse
from rest_framework.decorators import api_view
from students.models import Students
from . serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
      if(request.method == "GET"):
            students=Students.objects.all()
            serializer=StudentSerializer(students,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
      elif(request.method=="POST"):
                        serializer=StudentSerializer(data=request.data)
                        if(serializer.is_valid()):
                                serializer.save()
                                return Response (serializer.data,status=status.HTTP_201_CREATED)
                        return Response(serializer.errors,status=status.HTTP_404_BAD_Request)
      

@api_view(['GET','POST','PUT','DELETE'])
def studentDetailView(request, id):
    try:
       student = Students.objects.get(id=id)
    except Students.DoesNotExist:
            return Response(status=status.HTTP_404)
    
    if(request.method == "GET"):
            serializer=StudentSerializer(student)
            return Response(serializer.data,status=status.HTTP_200_OK)
    elif(request.method=="PUT"):
              serializer=StudentSerializer(student,data=request.data)
              if(serializer.is_valid()):
                      serializer.save()
                      return Response (serializer.data,status=status.HTTP_200_OK)
              else:
                  return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=="DELETE"):
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




