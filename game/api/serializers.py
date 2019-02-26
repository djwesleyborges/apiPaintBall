from rest_framework import serializers
from game.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    # Faz o link da imagem aparecer no json
    def to_representation(self, instance):
        representation = super(GameSerializer, self).to_representation(instance)
        representation['banner'] = instance.banner.url
        return representation