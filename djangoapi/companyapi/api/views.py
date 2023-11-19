from rest_framework import viewsets,status
from api.models import Device,TemperatureReading,HumidityReading
from api.serializer import DeviceSerializer,TemperatureReadingSerializer,HumidityReadingSerializer
from rest_framework.decorators import action
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from datetime import datetime
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Device.objects.all()
    serializer_class= DeviceSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class HumidityViewSet(viewsets.ModelViewSet):
    queryset = HumidityReading.objects.all()
    serializer_class = HumidityReadingSerializer

class TempViewSet(viewsets.ModelViewSet):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer
    


# class ReadingViewset(viewsets.GenericViewSet):
#     queryset = Reading.objects.all()
#     serializer_class = ReadingSerializer

    # @action(detail=True, methods=['get'])
    # def readings(self, request, pk=None):
    #     device_uid = pk
    #     parameter = request.query_params.get('parameter')
    #     start_on = datetime.strptime(request.query_params.get('start_on'), '%Y-%m-%dT%H:%M:%S')
    #     end_on = datetime.strptime(request.query_params.get('end_on'), '%Y-%m-%dT%H:%M:%S')

    #     readings = Reading.objects.filter(device__uid=device_uid, parameter=parameter, timestamp__gte=start_on, timestamp__lte=end_on)
    #     serializer = ReadingSerializer(readings, many=True)
    #     return Response(serializer.data)

# class DeviceGraphViewSet(viewsets.ModelViewSet):
#     def list(self, request):
#         device_uid = request.query_params.get('uid')  # Get device UID from the request query params
#         print(device_uid)
#         device = Device.objects.get_or_create(pk=device_uid)
#         print("Hello")
#             # Retrieve temperature readings fo the specified device
#         temperature_readings = TemperatureReading.objects.filter(pk=device)
            
#             # Extract required data for plotting
#         timestamps = [reading.timestamp for reading in temperature_readings]
#         temperatures = [reading.temperature for reading in temperature_readings]

#             # Pass the necessary data to the template for rendering
#         return Response({'device_uid': device_uid, 'timestamps': timestamps, 'temperatures': temperatures})
#         # Pass the device UID to the template for rendering33
