from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView
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


class FarmHistoryDetailView(DetailView):
    queryset = History.objects.all()
    context_object_name = 'history'
    template_name = 'farm/farm_history.html'

    def get_queryset(self):
        return self.queryset.filter(farm_id=self.kwargs.get('pk'))


class HelpTemplateView(TemplateView):
    template_name = 'pages/page_help.html'


class ProfileDetailView(TemplateView):
    template_name = 'registration/profile.html'

