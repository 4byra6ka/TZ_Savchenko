from rest_framework import serializers

from bitrix24.models import Bitrix24


class Bitrix24Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bitrix24
        fields = '__all__'