from pickle import PUT

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Continent
from .serializers import ContinentSerializer


@api_view(['GET', 'POST'])
def continent_list(request):
    if request.method == 'GET':
        continents = Continent.objects.all()
        serializer = ContinentSerializer(continents, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContinentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def continent_detail(request, pk):
    try:
        continent = Continent.objects.get(pk=pk)
    except Continent.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContinentSerializer(continent)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContinentSerializer(continent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        continent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
