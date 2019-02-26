from django.http import HttpResponse, Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from game.api.serializers import GameSerializer
from game.models import Game
from rest_framework.views import APIView


# class JSONResponse(HttpResponse):
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# class JogoList(APIView):
#     permission_classes = ([AllowAny, ])
#
#     def get(self, request):
#         """
#         Lista todos Jogos ou cria um novo Jogo
#         """
#         if request.method == 'GET':
#             jogo = Jogo.objects.all()
#             serializer = JogoSerializer(jogo, many=True)
#             return JSONResponse(serializer.data)
#
#     def post(self, request):
#         if request.method == 'POST':
#             data = JSONParser().parse(request)
#             serializer = JogoSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JSONResponse(serializer.data, status=201)
#             return JSONResponse(serializer.errors, status=400)



# class GameList(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request, format=None):
#         jogo = Game.objects.all()
#         serializer = GameSerializer(jogo, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, format=None):
#         serializer = GameSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GameList(ModelViewSet):
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        return queryset

    def list(self, request, *args, **kwargs):
        return super(GameList, self).list(request, *args, **kwargs)


class GameDetails(APIView):
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        jogo = self.get_object(pk)
        serializer = GameSerializer(jogo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        jogo = self.get_object(pk)
        serializer = GameSerializer(jogo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        jogo = self.get_object(pk)
        jogo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
