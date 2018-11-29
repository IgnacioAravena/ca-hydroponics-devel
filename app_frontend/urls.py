from django.urls import path
from .views import FarmListView, FarmDetailView, FarmHistoryDetailView
from .views import HelpTemplateView, ProfileDetailView


urlpatterns = [
    path('farm', FarmListView.as_view(), name="farm-list"),
    path('farm/<pk>/', FarmDetailView.as_view(), name='farm-detail'),
    path('farm/<pk>/history', FarmHistoryDetailView.as_view(), name='farm-history'),

    path('help', HelpTemplateView.as_view(), name="help"),

    path('accounts/profile', ProfileDetailView.as_view(), name="profile")

]

"""
    /                   loading screen
    /password/change    first pass change
    
    sugerencias         a
    fotos y videos      a
    configuracion       a

    mensajes            a

"""