
from django.contrib import admin
from django.urls import path, include
from hotels.views import *

urlpatterns = [
     path('index', index, name="home-page"),
     path('rooms', rooms, name="rooms"),
     path('reservation', reservation, name="reservation"),
     path('activities', activities, name="activities"),
     path('contact', contact, name="contact"),
     path('details', details, name="details"),
     path('guests/', GusestsList.as_view(), name="gosti"),
     path('getrooms', GetRoomsView.as_view(), name="roomsAPI"),
     path('getrooms/<int:pk>', ChangeRoomsView.as_view(), name="ChengeRoomsAPI"),
     path('gethotels', GetHotelsView.as_view(), name="hotelsAPI"),
     path('gethotels/<int:pk>', ChangeHotelsView.as_view(), name="ChengeHotelsAPI"),
     path('getdescription', GetDescriptionView.as_view(), name="descriptionAPI"),
     path('getdescription/<int:pk>', ChangeDescriptionView.as_view(), name="ChengeDetailsAPI"),
]

