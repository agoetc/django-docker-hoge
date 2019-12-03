from rest_framework import serializers

from .models import Hoge


class HogeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoge
        fields = ('id', 'hoge', 'customer')
