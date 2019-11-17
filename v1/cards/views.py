from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CardView(APIView):
    def get(self, request):
        print('REQ.VERSION: ' + request.version)

        return Response(data="here we go", status=status.HTTP_200_OK)
