# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer

class SensorApiView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        sensor_new = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'post': model_to_dict(sensor_new)})

    def put(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorSerializer(instance=sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data})

    def delete(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        sensor.delete()
        return Response({'message': f'Датчик с id={pk} был удалён'})


class MeasurementsApiView(APIView):

    def post(self, request):
        sensor_id = Sensor.objects.get(id=int(request.data['sensor_id']))
        measurement_new = Measurement.objects.create(
            sensor_id=sensor_id,
            temperature=request.data['temperature']
        )
        return Response({'post': model_to_dict(measurement_new)})