from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from advertisement.api import serializers
from advertisement.models import Advertisement
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from advertisement.api.serializers import AdvertisementSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class AdvertisementListViewSet(ModelViewSet):
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        queryset = Advertisement.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        return super(AdvertisementListViewSet, self).list(request, *args, **kwargs)

    def returnAdvertisement(self, request):
        ad = Advertisement.objects.filter(created_by=request.user)
        serializer = AdvertisementSerializer(ad)
        return serializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        title = self.request.data['title']
        address = self.request.data['address']
        complement = self.request.data['complement']
        zip_code = self.request.data['zip_code']
        price = self.request.data['price']
        description = self.request.data['description']
        ad = Advertisement.objects.create(title=title, address=address, complement=complement,
                                          zip_code=zip_code, price=price, description=description,
                                          created_by=user)
        ad.save()
        # ad = get_object_or_404(Advertisement.objects.all(pk=request.user.id))
        # serializer = serializers.AdvertisementSerializer(ad)
        # return Response(serializer.data)
        json = self.returnAdvertisement(request)
        content = {'Message': 'Your Advertisement has been created with success'}

        return Response(json.data, status=status.HTTP_201_CREATED)

    # GET COM PASSAGEM DE PARAMETRO retorna um usuario especifico http://127.0.0.1:8000/ad/1/
    def retrieve(self, request, *args, **kwargs):
        return super(AdvertisementListViewSet, self).retrieve(request, *args, **kwargs)

    # PUT
    def update(self, request, *args, **kwargs):
        return super(AdvertisementListViewSet, self).update(request, *args, **kwargs)

    # PATCH
    def partial_update(self, request, *args, **kwargs):
        return super(AdvertisementListViewSet, self).partial_update(request, *args, **kwargs)

# class AdvertisementListViewSet(viewsets.ViewSet):
#
#
#     def list(self, request):
#         queryset = Advertisement.objects.all()
#         serializer = AdvertisementSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     # GET COM PASSAGEM DE PARAMETRO retorna um anincio especifico http://127.0.0.1:8000/ad/1/
#     def retrieve(self, request, pk=None):
#         ad = get_object_or_404(Advertisement.objects.filter(pk=pk))
#         serializer = serializers.AdvertisementSerializer(ad)
#         return Response(serializer.data)