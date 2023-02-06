from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializers import StudentSerializer
from .models import Student


class StudentAPI(APIView):
    def get(self, request, format=None):
        id = request.data.get('id', None)

        if id is None: # when Id is not passed
            all_stu = Student.objects.all()
            serializer = StudentSerializer(all_stu, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                student = Student.objects.get(pk=id)
            except Student.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):

        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'Data inserted': 'Congrats data inserted successfuly', 'data is': serializer.data}
            return Response(res, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    
    def patch(self, request, format=None):
        id = request.data.get('id', None)

        if id is not None:
            try:
                student = Student.objects.get(pk=id)
            except Student.DoesNotExist: 
                return Response(status=status.HTTP_201_CREATED)
            else:
                serializer = StudentSerializer(student, data = request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    # return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors)
        else:
            res  = {'required': 'Id is required'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
                
