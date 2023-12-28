# news_integration/urls.py
from django.urls import path
from .views import get_environmental_news

urlpatterns = [
    path('get_environmental_news/', get_environmental_news, name='get_environmental_news'),
]
