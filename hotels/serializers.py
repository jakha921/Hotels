from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from hotels.models import Guests, Rooms, Hotels, description_list


class GuestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guests
        fields = ['hotel_name_number', 'FirstName', 'LastName']


class HotelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotels
        fields = "__all__"

class descriptionSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = description_list
        fields = "__all__" 


class RoomSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(
        slug_field='hotel_name', read_only=True)
    description = descriptionSerializer(many=True)

    class Meta:
        model = Rooms
        fields = ['id', 'room', 'price', 'quantity_room', 'type_room', 'room_img','description' ]

