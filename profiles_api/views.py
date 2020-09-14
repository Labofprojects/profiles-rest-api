from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format=None):
        """returns a list of API View features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post,patch,put delete)',
            'is similar to a traditional Django view',
            'Gives you the most control over application logic',
            'is mapped manually to urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})












#from django.shortcuts import render

# Create your views here.
