from user.models import User
from perfil.models import Perfil
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from perfil.api.serializers import PerfilSerializer


class UserListSerializer(ModelSerializer):
    perfil = PerfilSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'perfil')
        # read_only_fields = ('email',)

    def update(self, instance, validated_data):
        if validated_data.get('perfil').get('phone') is not None:
            instance.perfil.phone = validated_data.get('perfil').get('phone')

        if validated_data.get('perfil').get('city') is not None:
            instance.perfil.city = validated_data.get('perfil').get('city')
        instance.perfil.save()
        return instance


class UserRegistrationSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    """Serializers registration requests and creates a new user."""

    # Ensure passwords are at least 8 characters long, no longer than 128
    # characters, and can not be read by the client.
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    # The client should not be able to send a token along with a registration
    # request. Making `token` read-only handles that for us.
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['email', 'token', 'password', 'first_name', 'last_name', 'perfil']

    def create(self, validated_data):
        # Use the `create_user` method we wrote earlier to create a new user.
        perfil = validated_data['perfil']
        del validated_data['perfil']
        per = Perfil.objects.create(**perfil)
        user = User.objects.create_user(**validated_data)
        user.perfil = per
        user.save()
        return user
        # return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        if instance.perfil.phone is not None:
            instance.perfil.phone = validated_data.get('perfil').get('phone')

        if instance.perfil.state is not None:
            instance.perfil.state = validated_data.get('perfil').get('state')

        if instance.perfil.city is not None:
            instance.perfil.city = validated_data.get('perfil').get('city')

        return instance