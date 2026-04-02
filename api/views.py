from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from students.models import Students
from employee.models import Employee
from . serializers import StudentSerializer
from . serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@api_view(['GET','POST'])
def studentView(request):               # Function Based Method
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
def studentDetailView(request, id):          # Function Based Method
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


class Employees(APIView):            # Class Based Method
        def get(self,request):
                employees=Employee.objects.all()
                serializer=EmployeeSerializer(employees,many=True)
                return Response (serializer.data,status=status.HTTP_200_OK)
        
        def post(self,request):
                employee=request.data
                serializer=EmployeeSerializer(employee)
                if(serializer.is_valid()):
                        serializer.save()
                        return Response (serializer.data,status=status.HTTP_201_CREATED)
                else:
                     return Response(serializer.errors,status=status.HTTP_404_BAD_Request)
    

class EmployeeDetail(APIView):
        def get(self,request,id):
             try:
                employee=Employee.objects.get(id=id)
             except Employee.DoesNotExist:
                return Response(status=status.HTTP_404)
             
             serializer=EmployeeSerializer(employee)
             return Response(serializer.data,status=status.HTTP_200_OK)
        
        def put(self,request,id):
                employee=Employee.objects.get(id=id)
                serializer=EmployeeSerializer(employee,data=request.data)

                if(serializer.is_valid()):
                       serializer.save()
                       return Response (serializer.data,status=status.HTTP_200_OK)
                else:
                       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                
        def delete(aelf,request,id):
                employee=Employee.objects.get(id=id)
                employee.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
               

        


