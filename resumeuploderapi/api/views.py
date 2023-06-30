from django.shortcuts import render
from rest_framework.response import Response
from .models import Profile , ProfileSerlizer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class ProfileView(APIView):
    def post(self , request , format=None):
        serailizer = ProfileSerlizer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'msg':'Resume Upload Succesfully' , 'status':'Success','candidate':serailizer.data}, status=status.HTTP_201_CREATED)
        return Response(serailizer.errors)
    
    def get(self , request , format=None):
        candidates = Profile.objects.all()
        serlizer = ProfileSerlizer(candidates , many=True)
        return Response({'status':'success','candidates':serlizer.data},status=status.HTTP_200_OK)
            
