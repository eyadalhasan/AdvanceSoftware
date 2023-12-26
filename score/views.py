from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets

from .models import Score
from .serializer import serializerScore

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Max
from rest_framework import status


class ScoreViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Score.objects.all()
    serializer_class = serializerScore

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def get_max_score(self, request, *args, **kwargs):
        max_score = Score.objects.all().aggregate(
            max_score=Max("sustainability_score")
        )["max_score"]
        if not max_score:
            return Response(
                {"error": "No scores have been recorded yet."},
                status=status.HTTP_404_NOT_FOUND,
            )
        objs = Score.objects.filter(sustainability_score=max_score)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def get_by_score(self, request, pk, **kwargs):
        print(kwargs)
        objs = Score.objects.all().filter(sustainability_score=pk)
        serializer = self.get_serializer(objs, many=True)
        return Response(serializer.data)
