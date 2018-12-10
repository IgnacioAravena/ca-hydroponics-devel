from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Farm, History
from django.shortcuts import get_object_or_404

# Create your views here.
from django.views.generic.base import View


class FarmApi(View):

    def get(self, request, *args, **kwargs):
        print(request)
        uuid = request.GET.get('uuid')
        sensor_temp_air = request.GET.get('sensor_temp_air')
        sensor_temp_water = request.GET.get('sensor_temp_water')
        sensor_light = request.GET.get('sensor_light')
        sensor_wetness = request.GET.get('sensor_wetness')
        if uuid is None or sensor_temp_air is None or sensor_temp_water is None or sensor_light is None or sensor_wetness is None:
            return JsonResponse({'result': 'bad request'})

        farm = Farm.objects.filter(uuid=uuid)
        if farm is None:
            return JsonResponse({'result': 'farm not found'})

        farm = farm.get()
        history = History()
        history.farm = farm
        history.sensor_temp_air = farm.sensor_temp_air
        history.sensor_temp_water = farm.sensor_temp_water
        history.sensor_light = farm.sensor_light
        history.sensor_wetness = farm.sensor_wetness
        history.date = farm.last_date
        history.save()
        farm.sensor_temp_air = sensor_temp_air
        farm.sensor_temp_water = sensor_temp_water
        farm.sensor_light = sensor_light
        farm.sensor_wetness = sensor_wetness
        farm.save()

        data = {}
        return JsonResponse(data)
