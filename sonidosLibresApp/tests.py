from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime, timedelta
from sonidosLibresApp.models import Category, Audio, Artist, Album, Commentary, Convocation


class CategoryTest(APITestCase):

    def testListCategories(self):
        url = '/api/categories'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testDetailCategory(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.get().name, 'categoriaDemo')

        category = Category.objects.get(name='categoriaDemo')
        url = '/api/categories/' + str(category.id)
        data = {'name': 'newCategoryName',
                'image': 'https://www.google.com.co',
                'description': 'new Description'
                }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get().name, 'newCategoryName')

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ArtistsTest(APITestCase):

    def testListArtists(self):
        url = '/api/artists'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testDetailArtist(self):
        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.get().name, 'artistName')

        artist = Artist.objects.get(name='artistName')
        url = '/api/artists/' + str(artist.id)
        data = {'name': 'newArtistName',
                'image': 'https://www.yahoo.com'
                }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artist.objects.get().name, 'newArtistName')

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AlbumTest(APITestCase):

    def testListAlbums(self):
        url = '/api/albums'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testDetailAlbums(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Album.objects.get().title, 'albumTitle')

        album = Album.objects.get(title='albumTitle')
        url = '/api/albums/' + str(album.id)
        data = {
            "title": "newAlbumTitle",
            "image": "http://google.com",
            "categories": [str(category.id)],
            "artists": [str(artist.id)]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Album.objects.get().title, 'newAlbumTitle')

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AudioTest(APITestCase):

    def testListAudios(self):
        url = '/api/audios'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testDetailAudio(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        album = Album.objects.get(title='albumTitle')

        url = '/api/audios/'
        data = {
            "name": "d8d1b374-0fa4-4daf-ac9b-3e506662d78d",
            "title": "AudioDemo",
            "audioDownload": "http://www.dropbox.com",
            "audioPlay": "http://www.dropbox.com",
            "categories": [str(category.id)],
            "albums": [str(album.id)],
            "artists": [str(artist.id)]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Audio.objects.get().name, 'd8d1b374-0fa4-4daf-ac9b-3e506662d78d')

        audio = Audio.objects.get(name='d8d1b374-0fa4-4daf-ac9b-3e506662d78d')
        url = '/api/audios/' + str(audio.id)
        data = {
            "name": "6ef3058c-7110-46cf-8d76-794f49dc35e6",
            "title": "NewAudio",
            "audioDownload": "http://www.yahoo.com",
            "audioPlay": "http://www.yahoo.com",
            "categories": [str(category.id)],
            "albums": [str(album.id)],
            "artists": [str(artist.id)]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Audio.objects.get().name, '6ef3058c-7110-46cf-8d76-794f49dc35e6')

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CommentaryTest(APITestCase):

    def testListCommentaries(self):
        url = '/api/commentaries'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testDetailCommentaries(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        album = Album.objects.get(title='albumTitle')

        url = '/api/audios/'
        data = {
            "name": "d8d1b374-0fa4-4daf-ac9b-3e506662d78d",
            "title": "AudioDemo",
            "audioDownload": "http://www.dropbox.com",
            "audioPlay": "http://www.dropbox.com",
            "categories": [str(category.id)],
            "albums": [str(album.id)],
            "artists": [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        audio = Audio.objects.get(name='d8d1b374-0fa4-4daf-ac9b-3e506662d78d')

        url = '/api/commentaries/'
        data = {
            "commentary": "f5142b54-4113-4703-bf71-b1ee4fdb02d4",
            "audio": str(audio.id)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Commentary.objects.get().commentary, 'f5142b54-4113-4703-bf71-b1ee4fdb02d4')

        commentary = Commentary.objects.get(commentary='f5142b54-4113-4703-bf71-b1ee4fdb02d4')
        url = '/api/commentaries/' + str(commentary.id)
        data = {
            "commentary": "a0181681-afc5-440b-a2b7-36cdf5530873",
            "audio": str(audio.id)
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Commentary.objects.get().commentary, 'a0181681-afc5-440b-a2b7-36cdf5530873')

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AudioAlbumAssociationTest(APITestCase):

    def testAudioAlbumAssociation(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        album = Album.objects.get(title='albumTitle')

        url = '/api/audios/'
        data = {
            "name": "d8d1b374-0fa4-4daf-ac9b-3e506662d78d",
            "title": "AudioDemo",
            "audioDownload": "http://www.dropbox.com",
            "audioPlay": "http://www.dropbox.com",
            "categories": [str(category.id)],
            "albums": [str(album.id)],
            "artists": [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        audio = Audio.objects.get(name='d8d1b374-0fa4-4daf-ac9b-3e506662d78d')

        url = '/api/albumAudio/' + str(audio.id) + "/" + str(album.id) + "/"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class RateAudioTest(APITestCase):

    def testRateAudio(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        album = Album.objects.get(title='albumTitle')

        url = '/api/audios/'
        data = {
            "name": "d8d1b374-0fa4-4daf-ac9b-3e506662d78d",
            "title": "AudioDemo",
            "audioDownload": "http://www.dropbox.com",
            "audioPlay": "http://www.dropbox.com",
            "categories": [str(category.id)],
            "albums": [str(album.id)],
            "artists": [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        audio = Audio.objects.get(name='d8d1b374-0fa4-4daf-ac9b-3e506662d78d')

        i = 0
        while i <= 5:
            url = '/api/rateAudio/' + str(audio.id) + "/" + str(i) + "/"
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            i += 1
        while i <= 10:
            url = '/api/rateAudio/' + str(audio.id) + "/" + str(i) + "/"
            response = self.client.get(url, format='json')
            self.assertNotEquals(response.status_code, status.HTTP_200_OK)
            i += 1


class RateAlbumTest(APITestCase):

    def testRateAlbum(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        album = Album.objects.get(title='albumTitle')

        i = 0
        while i <= 5:
            url = '/api/rateAlbum/' + str(album.id) + "/" + str(i) + "/"
            response = self.client.get(url, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            i += 1
        while i <= 10:
            url = '/api/rateAlbum/' + str(album.id) + "/" + str(i) + "/"
            response = self.client.get(url, format='json')
            self.assertNotEquals(response.status_code, status.HTTP_200_OK)
            i += 1


class PlayAudioTest(APITestCase):

    def testPlayAudio(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        album = Album.objects.get(title='albumTitle')

        url = '/api/audios/'
        data = {
            "name": "d8d1b374-0fa4-4daf-ac9b-3e506662d78d",
            "title": "AudioDemo",
            "audioDownload": "http://www.dropbox.com",
            "audioPlay": "http://www.dropbox.com",
            "categories": [str(category.id)],
            "albums": [str(album.id)],
            "artists": [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        audio = Audio.objects.get(name='d8d1b374-0fa4-4daf-ac9b-3e506662d78d')

        i = audio.playCount
        url = '/api/play/' + str(audio.id)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        audio = Audio.objects.get(id=audio.id)
        self.assertEqual(audio.playCount, i + 1)


class DownloadAudioTest(APITestCase):

    def testDownloadAudio(self):
        url = '/api/categories/'
        data = {'name': 'categoriaDemo',
                'image': 'https://www.google.com.co',
                'description': 'Description'
                }
        self.client.post(url, data, format='json')
        category = Category.objects.get(name='categoriaDemo')

        url = '/api/artists/'
        data = {'name': 'artistName',
                'image': 'https://www.google.com.co'
                }
        self.client.post(url, data, format='json')
        artist = Artist.objects.get(name='artistName')

        url = '/api/albums/'
        data = {
            'title': 'albumTitle',
            'image': 'http://loudwire.com/files/2015/09/Nevermind.jpg',
            'categories': [str(category.id)],
            'artists': [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        album = Album.objects.get(title='albumTitle')

        url = '/api/audios/'
        data = {
            "name": "d8d1b374-0fa4-4daf-ac9b-3e506662d78d",
            "title": "AudioDemo",
            "audioDownload": "http://www.dropbox.com",
            "audioPlay": "http://www.dropbox.com",
            "categories": [str(category.id)],
            "albums": [str(album.id)],
            "artists": [str(artist.id)]
        }
        self.client.post(url, data, format='json')
        audio = Audio.objects.get(name='d8d1b374-0fa4-4daf-ac9b-3e506662d78d')

        i = audio.downloadsCount
        url = '/api/download/' + str(audio.id)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        audio = Audio.objects.get(id=audio.id)
        self.assertEqual(audio.downloadsCount, i + 1)


class CreateUsersTest(APITestCase):

    def testCreateArtists(self):
        self.client.get('/api/createGroups', format='json')
        url = '/api/signUp/artist'
        data = {'email': 'artista1@abc.com',
                'first_name': 'ArtistaNombre',
                'last_name': 'ArtistaApellido',
                'username': 'artista1@abc.com',
                'password': 'artista',
                'gender': 'M',
                'account': '123456789',
                'description': 'abcd efgh ijkl',
                'birthday': '2000-01-01',
                'nickname': 'artist',
                'image': 'www.yahoo.com'
                }
        self.client.post(url, data, format='json')
        artist = User.objects.get(first_name='ArtistaNombre')
        self.assertEqual(artist.username, 'artista1@abc.com')

    def testCreateAgents(self):
        self.client.get('/api/createGroups', format='json')
        url = '/api/signUp/agent'
        data = {'email': 'artista1@abc.com',
                'first_name': 'Agent',
                'last_name': 'Agent',
                'username': 'agent1@abc.com',
                'password': 'agent'
                }
        self.client.post(url, data, format='json')
        agent = User.objects.get(first_name='Agent')
        self.assertEqual(agent.username, 'agent1@abc.com')

    def testCreateAdmins(self):
        url = '/api/signUp/admin'
        self.client.get('/api/createGroups', format='json')
        data = {'email': 'admin1@abc.com',
                'first_name': 'Admin',
                'last_name': 'Admin',
                'username': 'admin1@abc.com',
                'password': 'admin'
                }
        self.client.post(url, data, format='json')
        admin = User.objects.get(first_name='Admin')
        self.assertEqual(admin.username, 'admin1@abc.com')


class ConvocationTest(APITestCase):

    def testListConvocation(self):
        url = '/api/convocations'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testDetailConvocation(self):
        self.client.get('/api/createGroups', format='json')
        url = '/api/signUp/agent'
        data = {'email': 'artista1@abc.com',
                'first_name': 'Agent',
                'last_name': 'Agent',
                'username': 'agent1@abc.com',
                'password': 'agent'
                }
        self.client.post(url, data, format='json')
        agent = User.objects.get(first_name='Agent')

        url = '/api/convocations/'
        data = {
            "name": "NombreConvocatoria",
            "title": "TituloConvocatoria",
            "detail": "Detalle",
            "typeConvocation": "PUB",
            "terms": "www.google.com",
            "dateInit": str(datetime.today()),
            "dateEnd": str(datetime.today() + timedelta(days=1)),
            "dateLimit": str(datetime.today() + timedelta(days=2)),
            "dateResults": str(datetime.today() + timedelta(days=10)),
            "status": "U",
            "agent": str(agent.id)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Convocation.objects.get().name, 'NombreConvocatoria')

        convocation = Convocation.objects.get(name='NombreConvocatoria')
        url = '/api/convocations/' + str(convocation.id)
        data = {
            "name": "NewNombreConvocatoria",
            "title": "NewTituloConvocatoria",
            "detail": "NewDetalle",
            "typeConvocation": "PRI",
            "terms": "www.yahoo.com",
            "dateInit": str(datetime.today()),
            "dateEnd": str(datetime.today() + timedelta(days=1)),
            "dateLimit": str(datetime.today() + timedelta(days=2)),
            "dateResults": str(datetime.today() + timedelta(days=10)),
            "status": "P",
            "agent": str(agent.id)
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Convocation.objects.get().name, 'NewNombreConvocatoria')

        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

