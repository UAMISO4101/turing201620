from random import randint
from tokenize import Token

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, Group
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
    ArtistSerializer, ConvocationSerializer, UserSerializer, ConvocationAudioSerializer, AgenteSerializer, AdminSerializer, ConvocationVotingSerializer, \
    DonationSerializer
from .models import Audio, Category, Album, Commentary, Artist, Convocation, ConvocationAudio,ConvocationVoting, \
    Donation
from datetime import datetime, date, time, timedelta
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id = token.user_id)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'id': token.user_id, 'user': serializer.data})

class CreateAdminView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = AdminSerializer

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

class CreateAgentView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = AgenteSerializer


def setAudioQuerySet(self):
    is_admin = False
    for group in self.request.user.groups.all():
        if group.name == 'admins':
            is_admin = True
            break
    if not is_admin:
        queryset=Audio.objects.filter(vetoed=False, active=True)
    else:
        queryset = Audio.objects.all()
    return queryset


class AudioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    serializer_class = AudioSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('title', 'rating', 'playCount', 'downloadsCount','uploadDate','numOfRatings', 'categories','albums', 'artists', 'vetoed', 'active')
    ordering_fields = ('title', 'rating', 'playCount', 'downloadsCount','uploadDate','numOfRatings')

    def get(self, request, *args, **kwargs):
        self.queryset = setAudioQuerySet(self)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.queryset = setAudioQuerySet(self)
        return self.create(request, *args, **kwargs)


class AudioDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    serializer_class = AudioSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = setAudioQuerySet(self)
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.queryset = setAudioQuerySet(self)
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.queryset = setAudioQuerySet(self)
        return self.destroy(request, *args, **kwargs)


class ArtistList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArtistDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CategoryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AlbumList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('title', 'rating', 'categories','numOfRatings','artists','id')
    ordering_fields = ('title', 'rating', 'categories','numOfRatings','artists','id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AlbumDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentaryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentaryDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
    pagination_class = StandardResultsSetPagination


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AudioAlbumAssociation(APIView):
    def get(self,request,idAudio, idAlbum,format=None):
        audio = Audio.objects.get(id=idAudio)
        album = Album.objects.get(id=idAlbum)
        album.audios.add(audio)
        serializer = AudioSerializer(audio)
        return Response(serializer.data)

    def delete(self, request, idAudio, idAlbum, format=None):
        audio = Audio.objects.get(id=idAudio)
        album = Album.objects.get(id=idAlbum)
        album.audios.remove(audio)
        serializer = AudioSerializer(audio)
        return Response(serializer.data)

class RateAudio(APIView):
    def get(self,request,idAudio, rating,format=None):
        audio = Audio.objects.get(id=idAudio)
        newRate = ((audio.rating * audio.numOfRatings) + int(rating))/(audio.numOfRatings + 1)
        audio.rating=newRate
        audio.numOfRatings += 1
        audio.save()
        serializer = AudioSerializer(audio)
        return Response(serializer.data)

class RateAlbum(APIView):
    def get(self,request,idAlbum, rating,format=None):
        album = Album.objects.get(id=idAlbum)
        newRate = ((album.rating * album.numOfRatings) + int(rating))/(album.numOfRatings + 1)
        album.rating=newRate
        album.numOfRatings += 1
        album.save()
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

class PlayAudio(APIView):
    def get(self,request,idAudio,format=None):
        audio = Audio.objects.get(id=idAudio)
        audio.playCount += 1
        audio.save()
        serializer = AudioSerializer(audio)
        return Response(serializer.data)

class DownloadAudio(APIView):
    def get(self,request,idAudio,format=None):
        audio = Audio.objects.get(id=idAudio)
        audio.downloadsCount += 1
        audio.save()
        serializer = AudioSerializer(audio)
        return Response(serializer.data)


class CategoriesTopRating(APIView):
    def get(self,request,size,format=None):
        resp = []
        categories = Category.objects.all()
        for c in categories:
            cat = {}
            cat['id']=c.pk
            cat['name']=c.name
            cat['image'] = c.image
            audios = Audio.objects.filter(categories__in=[c.pk], vetoed=False, active=True).order_by('-rating')[:int(size)]
            audList = []
            var = 0
            for a in audios:
                aud = {}
                aud['id'] = a.pk
                aud['name'] = a.name
                aud['title'] = a.title
                aud['audioDownload'] = a.audioDownload
                aud['audioPlay'] = a.audioPlay
                aud['playCount'] = a.playCount
                aud['downloadsCount'] = a.downloadsCount
                aud['rating'] = a.rating
                aud['uploadDate'] = a.uploadDate

                artists = Artist.objects.filter(audios__in=[a.pk]).order_by('name')
                artList = []
                for t in artists:
                    art = {}
                    art['id'] = t.pk
                    art['name'] = t.name
                    art['image'] = t.image
                    artList.append(art)

                aud['artists'] = artList

                audList.append(aud)
                if var == int(size)-1:
                    break

            cat['audios']=audList
            resp.append(cat)

        return JsonResponse(resp, safe=False)

class ConvocationList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Convocation.objects.all()
    serializer_class = ConvocationSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('title', 'agent', 'typeConvocation', 'status')
    ordering_fields = ('title', 'agent', 'typeConvocation', 'status')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ConvocationDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Convocation.objects.all()
    serializer_class = ConvocationSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ConvocationExpired(APIView):
    def get(self,request,format=None):
        max = 5
        dateToday = date.today()
        dateExprired = date.today() + timedelta(days=7)
        expired = []
        convocations = Convocation.objects.all()

        for c in convocations:
            serializaser = ConvocationSerializer(c)
            if len(expired) == 5:
                break
            if dateToday <= c.dateEnd <= dateExprired:
                expired.append(serializaser.data)

        return JsonResponse(expired, safe=False)


class Registrar(APIView):

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(username = request.data.get('username')).count()>0:
                message = 'El username no está disponible'
                response = JsonResponse({'error': message}, status=409)
                return response
            elif User.objects.filter(email = request.data.get('email')):
                message = 'El correo electrónico ya se encuentra registrado'
                response = JsonResponse({'error': message}, status=409)
                return response
            else:
              serializer.save()
              return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConvocationAudios(APIView):
    def get(self,request,idConvocation,format=None):
        audios = []
        convocationAudios = ConvocationAudio.objects.filter(convocation = idConvocation)
        for c in convocationAudios:
            audio = c.audio
            serializer = AudioSerializer(audio)
            audios.append(serializer.data)
        return JsonResponse(audios, safe=False)

class ConvocationAudioAsociation(APIView):
    def get(self,request,idAudio,idConvocation,format=None):
        audio = Audio.objects.get(id=idAudio)
        convocation=Convocation.objects.get(id=idConvocation)
        convocatioAudio = ConvocationAudio()
        convocatioAudio.audio=audio
        convocatioAudio.convocation=convocation
        convocatioAudio.save()
        serializer = ConvocationAudioSerializer(convocatioAudio)
        return Response(serializer.data)

class ConvocationAudioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = ConvocationAudio.objects.all()
    serializer_class = ConvocationAudioSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('convocation', 'audio', 'votes')
    ordering_fields = ('convocation', 'audio', 'votes')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ConvocationAudioDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ConvocationAudio.objects.all()
    serializer_class = ConvocationAudioSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class VotingAudio(APIView):
    def get(self,request,idConvocation,idAudio,idArtist,format=None):
        if ConvocationVoting.objects.filter(convocation=idConvocation,artist=idArtist).count() == 0:
            convocationAudio = ConvocationAudio.objects.get(convocation=idConvocation,audio=idAudio)
            convocationAudio.votes += 1
            convocationAudio.save()
            convocationVoting = ConvocationVoting()
            convocation=Convocation.objects.get(id=idConvocation)
            artist=Artist.objects.get(id=idArtist)
            convocationVoting.convocation = convocation
            convocationVoting.artist = artist
            convocationVoting.save()
            resp = 0
            return JsonResponse(resp, safe=False)
        else:
            resp = 1
            return JsonResponse(resp, safe=False)


class GetVote(APIView):
    def get(self,request,idConvocation,idAudio,format=None):
        convocationAudio = ConvocationAudio.objects.get(convocation=idConvocation,audio=idAudio)
        serializer = ConvocationAudioSerializer(convocationAudio)
        resp=convocationAudio.votes
        return JsonResponse(resp, safe=False)


class CreateGroups(APIView):
    def get(self, request):
        g = Group.objects.create(name='admins')
        g = Group.objects.create(name='artists')
        g = Group.objects.create(name='agents')
        response = JsonResponse({'OK': 'Grupos creados'}, status=200)
        return response

class DonationList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('date', 'idArtist', 'idUser', 'amount')
    ordering_fields = ('date', 'idArtist', 'idUser', 'amount')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TopRandomArtists(APIView):
    def get(self,request,size,format=None):
        resp = []
        artists = Artist.objects.all()
        for i in range (0, int(size)):
            pos = randint(0,artists.count()-1)
            serializer = ArtistSerializer(artists[pos])
            resp.append(serializer.data)
        return JsonResponse(resp, safe=False)

class TopAlbums(APIView):
    def get(self,request,format=None):
        resp = []
        added = {}
        audios = Audio.objects.all().order_by('-audioPlay')
        for i in range (0, audios.count()):
            audio = audios[i]
            album = Album.objects.filter(audios__in=[audio.pk])[0]
            serializer = AlbumSerializer(album)
            if added.get(album.title) is None:
                resp.append(serializer.data)
                added[album.title] = 'OK'
            if(len(resp) >= 5):
                break
        return JsonResponse(resp, safe=False)