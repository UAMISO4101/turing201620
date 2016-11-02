import copy

from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Audio, Category, Album, Commentary, Artist,Convocation,ConvocationAudio

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


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary


class ConvocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocation

class ConvocationAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvocationAudio


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name','groups',)
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
        g = Group.objects.get(name='artists')
        g.user_set.add(user)
        g.save()
        user.save()

        return user

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name','groups',)
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
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name','groups',)
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

        return user