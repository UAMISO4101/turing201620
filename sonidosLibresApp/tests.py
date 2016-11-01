from rest_framework import status
from rest_framework.test import APITestCase

from sonidosLibresApp.models import Category, Audio, Artist, Album, Commentary

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