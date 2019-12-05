from rest_framework.response import Response
from forum.models import Publication, Answer
from rest_framework.viewsets import ModelViewSet
from forum.api.serializers import PublicationListSerializer, AnswerListSerializer, PublicationDetailsSerializer

class PublicationListViewSet(ModelViewSet):
    serializer_class = PublicationListSerializer

    def get_queryset(self):
        queryset = Publication.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        return super(PublicationListViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PublicationListViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # usando um serializador customizado para trazer os detalhes do post
        serializer = PublicationDetailsSerializer(instance=instance)
        return Response(serializer.data)

    # PUT
    def update(self, request, *args, **kwargs):
        return super(PublicationListViewSet, self).update(request, *args, **kwargs)

    # PATCH
    def partial_update(self, request, *args, **kwargs):
        return super(PublicationListViewSet, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        delete = super(PublicationListViewSet, self).destroy(request, *args, **kwargs)
        return delete

class AnswerListViewSet(ModelViewSet):
    serializer_class = AnswerListSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        return super(AnswerListViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(AnswerListViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(AnswerListViewSet, self).retrieve(request, *args, **kwargs)
