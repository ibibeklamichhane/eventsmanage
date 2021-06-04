from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('events/', views.get_all_events, name='allevent'),

]
