from .views import HomePageview
from django.urls import path

urlpatterns = [
    path('', HomePageview.as_view(), name='home'),
    path('about/', HomePageview.as_view(template_name='about.html'), name='about'),
]