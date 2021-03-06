
from django.contrib.auth.models import User, Group
import json
from rest_framework import serializers

from .models import Audio, Category, Album, Commentary, Artist,Convocation,ConvocationAudio,ConvocationVoting, Donation


class AudioCreate(serializers.ModelSerializer):
    class Meta:
        model = Audio

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category

class CategoryWithAudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = ['id','name', 'image','audios']

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donation


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary


class ConvocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocation

class ConvocationAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvocationAudio

class ConvocationVotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvocationVoting



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        datos = self.initial_data
        user.artist.gender = datos['gender']
        user.artist.account = datos['account']
        user.artist.description = datos['description']
        user.artist.birthday = datos['birthday']
        user.artist.nickname = datos['nickname']
        user.artist.image = datos['image']

        g = Group.objects.get(name='artists')
        g.user_set.add(user)
        g.save()
        user.save()

        return user

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        g = Group.objects.get(name='admins')
        g.user_set.add(user)
        g.save()
        user.save()
        return user

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        g = Group.objects.get(name='agents')
        g.user_set.add(user)
        g.save()
        user.save()
        return user

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)