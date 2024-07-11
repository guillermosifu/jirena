from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from tracking.models import *
from .serializers import (
    TrackingRegistrosSerializer
)

class TrackingRegistrosView(APIView):
    
    def get(self,request):
        data = TrackingRegistros.objects.all()
        serializer = TrackingRegistrosSerializer(data,many=True)
        context = {
            'data':serializer.data
        }
        return Response(context)
