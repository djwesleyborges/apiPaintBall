from rest_framework import serializers

from advertisement.models import Advertisement
from rest_framework.serializers import ModelSerializer


class AdvertisementSerializer(ModelSerializer):
    created_by = serializers.UUIDField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Advertisement
        fields = ('title', 'address', 'complement', 'zip_code',
                  'price', 'description', 'created_at', 'update_at', 'created_by')

    # def create(self, validated_data):
    #     user = self._context.get('request').user
    #     title = validated_data['title']
    #     address = validated_data['address']
    #     complement = validated_data['complement']
    #     zip_code = validated_data['zip_code']
    #     price = validated_data['price']
    #     description = validated_data['description']
    #     created_by = user
    #
    #     advertisement = Advertisement.objects.create(title=title, address=address,complement=complement,
    #                                                  zip_code=zip_code ,price=price, description=description,
    #                                                  created_by=created_by)
    #     advertisement.save()
    #     return advertisement

    def create(self, validated_data):
        #user = self._context.get('request').user
        instance = Advertisement.objects.create(**validated_data)
        #instance.created_by = user
        instance.save()
        return instance