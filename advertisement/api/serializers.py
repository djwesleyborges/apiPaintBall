from advertisement.models import Advertisement
from rest_framework.serializers import ModelSerializer


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        user = self._context.get('request').user
        title = validated_data['title']
        address = validated_data['address']
        complement = validated_data['complement']
        zip_code = validated_data['zip_code']
        price = validated_data['price']
        description = validated_data['description']
        created_by = user

        advertisement = Advertisement.objects.create(title=title, address=address,complement=complement,
                                                     zip_code=zip_code ,price=price, description=description,
                                                     created_by=created_by)
        advertisement.save()
        return advertisement
