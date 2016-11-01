from tokenize import Token

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token

from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import filters
from sonidosLibresApp.customPagination import StandardResultsSetPagination
from sonidosLibresApp.serializers import AudioSerializer, CategorySerializer, AlbumSerializer, CommentarySerializer, \
    ArtistSerializer, ConvocationSerializer, UserSerializer
from .models import Audio, Category, Album, Commentary, Artist, Convocation
from datetime import datetime, date, time, timedelta
from rest_framework.response import Response

class misAudiosMasVotados(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        user = request.user

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)