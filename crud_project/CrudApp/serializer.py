from rest_framework import serializers
from . models import VehicleModel


class VehicleModelSerializer(serializers.ModelSerializer):
    
    # class Meta is the inner class of your model class.
    # It is used to change the behavior of the fields like selecting specific fields.
    class Meta:
        model = VehicleModel
        fields = '__all__'