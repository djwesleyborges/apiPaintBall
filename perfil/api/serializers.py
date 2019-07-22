from rest_framework import serializers
from perfil.models import Perfil


class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = '__all__'
        # read_only_fields = ('imagem',)

    # def to_representation(self, instance):
    #     representation = super(PerfilSerializer, self).to_representation(instance)
    #     representation['imagem'] = instance.imagem.url
    #     return representation