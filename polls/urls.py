from django.urls import path
from . import views as v
from django.views.generic.base import TemplateView
from django.conf import settings
from accounts import views as va

urlpatterns = [
    path('', v.HomeView.as_view(), name='home'),
    path('sight/<slug>/', v.SightDatailView.as_view(), name ='sight'),
    path('howitworks/', TemplateView.as_view(template_name='howitworks.html'), name='howitworks'),
    path('prices/', v.PricesView.as_view(), name='prices'),
    path('add/<pk>/', v.PricesDatailView.as_view(), name='add'),
    path('faq/', TemplateView.as_view(template_name='faq.html'), name='faq'),
]
