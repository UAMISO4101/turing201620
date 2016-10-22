from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import filters
from sonidosLibresApp.customPagination import StandardResultsSetPagination
from sonidosLibresApp.serializers import AudioSerializer, CategorySerializer, AlbumSerializer, CommentarySerializer, \
    ArtistSerializer
from .models import Audio, Category, Album, Commentary, Artist
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')

class AudioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.OrderingFilter,)
    pagination_class = StandardResultsSetPagination
    filter_fields = ('title', 'rating', 'playCount', 'downloadsCount','uploadDate','numOfRatings', 'categories','albums')
    ordering_fields = ('title', 'rating', 'playCount', 'downloadsCount','uploadDate','numOfRatings')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AudioDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
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
            serializer = CategorySerializer(c)
            cat['id']=c.pk
            cat['name']=c.name
            cat['image'] = c.image
            audios = Audio.objects.filter(categories__in=[c.pk]).order_by('-rating')
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