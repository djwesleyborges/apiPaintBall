from advertisement.models import Advertisement
from rest_framework.serializers import ModelSerializer


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
