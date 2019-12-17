from rest_framework import serializers

from .models import Todo, Customer, Profile
from hoge.serializers import HogeSerializer


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'todo')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_id', 'email_address', 'first_name', 'last_name')


class CustomerSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=False)
    # hoges = HogeSerializer(many=True)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(**profile_data)
        customer = Customer.objects.create(profile=profile, **validated_data)
        return customer

    class Meta:
        model = Customer
        fields = ('customer_id', 'profile')
