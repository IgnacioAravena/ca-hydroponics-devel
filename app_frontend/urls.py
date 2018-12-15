from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import SplashScreenView
from .views import FarmListView, FarmDetailView, FarmHistoryDetailView
from .views import HelpTemplateView, ProfileDetailView, TipsTemplateView
from .views import ChatView


urlpatterns = [
    path('', SplashScreenView.as_view(), name="splash_screen"),

    path('farm', login_required(FarmListView.as_view())),
    path('farm/<pk>/', login_required(FarmDetailView.as_view())),
    path('farm/<pk>/history', login_required(FarmHistoryDetailView.as_view())),

    path('help', HelpTemplateView.as_view(), name="help"),
    path('tips', TipsTemplateView.as_view(), name="tips"),
    path('chat', ChatView.as_view()),

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