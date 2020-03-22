from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class first(APIView):
    def get(self, request, ):
        print('0707 我是01')
    pass