from rest_framework import generics
from . models import VehicleModel
from .serializers import VehicleModelSerializer

class VehicleDetail(generics.RetrieveUpdateAPIView):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer