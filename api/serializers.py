from rest_framework import serializers
from students.models import Students

class StudentSerializer(serializers.ModelSerializer):
      class meta:
            model=Students
            fields="__all__"