from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from sonidosLibresApp import views

router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^audios/?$', views.AudioList.as_view()),
    url(r'^audios/(?P<pk>[0-9]+)/?$', views.AudioDetail.as_view()),
    url(r'^artists/?$', views.ArtistList.as_view()),
    url(r'^artists/(?P<pk>[0-9]+)/?$', views.ArtistDetail.as_view()),
    url(r'^categories/?$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/?$', views.CategoryDetail.as_view()),
    url(r'^albums/?$', views.AlbumList.as_view()),
    url(r'^albums/(?P<pk>[0-9]+)/?$', views.AlbumDetail.as_view()),
    url(r'^commentaries/?$', views.CommentaryList.as_view()),
    url(r'^commentaries/(?P<pk>[0-9]+)/?$', views.CommentaryDetail.as_view()),
    url(r'^albumAudio/(?P<idAudio>[0-9]+)/(?P<idAlbum>[0-9]+)/?$', views.AudioAlbumAssociation.as_view()),
    url(r'^rateAudio/(?P<idAudio>[0-9]+)/(?P<rating>[0-5])/?$', views.RateAudio.as_view()),
    url(r'^rateAlbum/(?P<idAlbum>[0-9]+)/(?P<rating>[0-5])/?$', views.RateAlbum.as_view()),
    url(r'^play/(?P<idAudio>[0-9]+)/?$', views.PlayAudio.as_view()),
    url(r'^download/(?P<idAudio>[0-9]+)/?$', views.DownloadAudio.as_view()),
    url(r'^categoriesTopRating/(?P<size>[0-9]+)/?$', views.CategoriesTopRating.as_view()),

]

#urlpatterns =format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
