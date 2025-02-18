from rest_framework.views import APIView
from rest_framework import status,serializers
from rest_framework.response import Response

from .serializers import *
from .models import *

# Create your views here.
class DiaryView(APIView):
    def get(self,request):
       try:
              diary = Diary.objects.all()
              serializer = DiarySerializer(diary,many=True)
              return Response(serializer.data, status=status.HTTP_200_OK)
       except Exception as e:
            return Response({'Message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    def post(self,request):
       try:
            serializer = DiarySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save( )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       except Exception as e:
           return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
class DiaryDetailView(APIView):
    def get(self,request,id):
        try:
            diary = Diary.object.get(id=id)
            serializer = DiarySerializer(diary)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def put(self,request,id):
        try:
            diary = Diary.object.get(id=id)
            serializer = DiarySerializer(instance=diary, data=request.data, partial=True)
            if serializer.is_valid:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def delete(self,request,id):
        try:
            diary = Diary.object.get(id=id)
            diary.delete()
            return Response({"Message":str(e)}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
class RegisterUserView(APIView):
    def post(self, request):
        try:
            serializer = RegisterUserView(data=request.serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error" : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

 

            
      


    

