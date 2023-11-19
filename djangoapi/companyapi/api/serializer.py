from rest_framework import serializers
from api.models import TemperatureReading,HumidityReading,Device

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = Device
        fields = "__all__"

class TemperatureReadingSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = TemperatureReading
        fields = "__all__"

class HumidityReadingSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model = HumidityReading
        fields = "__all__"

# class ReadingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reading
#         fields = '__all__'