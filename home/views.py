import imp
from unicodedata import east_asian_width
from urllib import request
from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from . serializers import *
# Create your views here.
from rest_framework.parsers import MultiPartParser

class HandleFilesURL(APIView):
    parser_classes  = [MultiPartParser] 
    def post(self,request):
       try:
        #    data= request.data
           serializer= FileListSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(
                   {'status':200,'msg':'Files Uploaded Successfully.', 'data':serializer.data}
                   
                   )

           return Response({'status':400, 'error': serializer.errors})


       except Exception as e:
            print(e)

            




def index(request):
    
    return render(request , 'index.html')












