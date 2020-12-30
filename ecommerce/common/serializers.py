from rest_framework import serializers


class RegistrationRequestSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, min_length=1)
    password = serializers.CharField(required=True, min_length=6, max_length=128)
    email = serializers.EmailField(required=True)


class SubmitOrderRequestSerializer(serializers.Serializer):
    house = serializers.CharField(required=True, min_length=1)
    lat = serializers.FloatField(required=True, min_value=-90, max_value=90)
    long = serializers.FloatField(required=True, min_value=-180, max_value=180)