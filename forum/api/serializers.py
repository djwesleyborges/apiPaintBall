from rest_framework import serializers
from forum.models import Publication , Answer
from rest_framework.serializers import ModelSerializer


class PublicationListSerializer(ModelSerializer):
    # answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Publication
        #fields = '__all__, answer'
        fields = ['id', 'title', 'description', 'created', 'active', 'create_by']

    def create(self, validated_data):
        #answer_data = validated_data.pop('answer')
        instance = Publication.objects.create(**validated_data)
        #Answer.objects.create(**answer_data)
        return instance
        # instance = Publication.objects.create(**validated_data)
        # instance.save()
        # return instance


    # def create(self, validated_data):
    #        profile_data = validated_data.pop('profile')
    #        user = User.objects.create(**validated_data)
    #        Profile.objects.create(user=user, **profile_data)
    #        return user

class AnswerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'description', 'created', 'active', 'create_by', 'publication']

    def create(self, validated_data):
        instance = Answer.objects.create(**validated_data)
        instance.save()
        return instance


class PublicationDetailsSerializer(serializers.ModelSerializer):
    """O que faz o vinculo do comentario com a publicação e o related_name no models do Answer
           ele e carregado na linha de comando abaixo e jogado para ser renderizado no fields"""
    answer = serializers.StringRelatedField(many=True)

    class Meta:
        model = Publication
        fields = ['id', 'title', 'description', 'created', 'active', 'create_by', 'answer']
