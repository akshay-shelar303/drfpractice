from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TodoModel
from .serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter


class MyViews(ModelViewSet):
    # def get(self, request):
    #     todo = TodoModel.objects.all()
    #     serializer = TodoSerializer(todo, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = TodoSerializer(data=request.data)
    #     if serializer.is_valid():

    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name','created_at','description']