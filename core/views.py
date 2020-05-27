from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# def test_view(request):
  # data = {
  #   'name': 'Parth',
  #   'age': 20
  # }
  # return  JsonResponse(data)

class TestView(APIView):
  def get(self, request, *args, **kwargs):
    data = {
      'name': 'Parth',
      'age': 20
    }
    return Response(data)