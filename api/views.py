from django.http import JsonResponse

# Create your views here.
def studentView(request):
      students={
            "name":"Ayush",
            "age":18,
            "college":"GNIOT",
            }
      
      return JsonResponse(students)
