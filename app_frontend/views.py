from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View

from app_backend.models import Farm, History


class SplashScreenView(TemplateView):
    template_name = 'pages/page_splash_screen.html'


class FarmListView(ListView):
    queryset = Farm.objects.all()
    context_object_name = 'farm_list'
    template_name = 'farm/farm_list.html'

    def get_queryset(self):
        return self.queryset.filter(owner_id=self.request.user.id)


class FarmDetailView(DetailView):
    queryset = Farm.objects.all()
    context_object_name = 'farm'
    template_name = 'farm/farm_detail.html'

    def get_queryset(self):
        return self.queryset.filter(id=self.kwargs.get('pk'))


class FarmHistoryDetailView(View):
    # queryset = History.objects.all()
    # context_object_name = 'history'
    template = 'farm/farm_history.html'

    # def get_queryset(self):
    #     return self.queryset.filter(farm_id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        farm_id = self.kwargs.get('pk')
        farm_name = ''
        labels = []
        serie_temp_air = []
        serie_temp_water = []
        serie_light = []
        serie_wetness = []

        objects = History.objects.filter(farm_id=farm_id)
        for obj in objects:
            farm_name = obj.farm.seed.name
            # labels.append(obj.date)
            labels.append(0)
            serie_temp_air.append(obj.sensor_temp_air)
            serie_temp_water.append(obj.sensor_temp_water)
            serie_light.append(obj.sensor_light)
            serie_wetness.append(obj.sensor_wetness)
        print(serie_wetness)
        return render(request, self.template, locals())


class HelpTemplateView(TemplateView):
    template_name = 'pages/page_help.html'


class TipsTemplateView(TemplateView):
    template_name = 'pages/page_tips.html'


class ProfileDetailView(TemplateView):
    template_name = 'registration/profile.html'
