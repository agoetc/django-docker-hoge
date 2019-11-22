from rest_framework import serializers

from .models import Todo, Customer, Profile


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

    class Meta:
        model = Customer
        fields = ('customer_id', 'profile')
