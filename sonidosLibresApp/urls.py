from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from sonidosLibresApp import views

router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/?$', views.CustomObtainAuthToken.as_view()),
    url(r'^signUp/artist/?$', views.CreateUserView.as_view()),
    url(r'^signUp/agent/?$', views.CreateAgentView.as_view()),
    url(r'^signUp/admin/?$', views.CreateAdminView.as_view()),
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
    url(r'^convocations/?$', views.ConvocationList.as_view()),
    url(r'^convocations/(?P<pk>[0-9]+)/?$',views.ConvocationDetail.as_view()),
    url(r'^convocationExpired/?$',views.ConvocationExpired.as_view()),
    url(r'^registrar/?$', views.Registrar.as_view()),
    url(r'^convocationExpired/?$',views.ConvocationExpired.as_view()),
    url(r'^convocationAudioAsociation/(?P<idAudio>[0-9]+)/(?P<idConvocation>[0-9]+)/?$',
        views.ConvocationAudioAsociation.as_view()),
    url(r'^convocationAudios/?$', views.ConvocationAudioList.as_view()),
    url(r'^convocationAudios/(?P<pk>[0-9]+)/?$', views.ConvocationAudioDetail.as_view()),
    url(r'^audiosConvocation/(?P<idConvocation>[0-9]+)/?$', views.ConvocationAudios.as_view()),
    url(r'^voting/(?P<idConvocationAudio>[0-9]+)/(?P<idArtist>[0-9]+)/?$', views.VotingAudio.as_view()),
    url(r'^createGroups/?$', views.CreateGroups.as_view()),
    url(r'^voting/(?P<idConvocation>[0-9]+)/(?P<idAudio>[0-9]+)/(?P<idArtist>[0-9]+)/?$', views.VotingAudio.as_view()),
    url(r'^getVote/(?P<idConvocation>[0-9]+)/(?P<idAudio>[0-9]+)/?$', views.GetVote.as_view()),
    url(r'^donations/?$', views.DonationList.as_view()),
    url(r'^topRandomArtists/(?P<size>[0-9]+)/?$', views.TopRandomArtists.as_view()),
    url(r'^topAlbums/?$', views.TopAlbums.as_view()),
    url(r'^search/(?P<query>\w+)/?$', views.Search.as_view()),
    url(r'^convocationAudioVoting/(?P<pk>[0-9]+)/?$', views.ConvocationAudioVoting.as_view()),
]

#urlpatterns =format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
