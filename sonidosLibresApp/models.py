
import django
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Category(models.Model):
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=40)
    image = models.URLField()
    description = models.TextField()
    relatedCategories = models.ManyToManyField('self',editable=False, blank=True)


class Artist(models.Model):
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "artists"

    name = models.CharField(max_length=40)
    user = models.OneToOneField(User, null=True, blank=True)
    image = models.URLField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.artist.save()

class Album (models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    rating = models.FloatField(editable=False, default = 0)
    numOfRatings = models.IntegerField(editable=False, default = 0)
    categories = models.ManyToManyField(Category,related_name="albums", blank=True)
    artists = models.ManyToManyField(Artist, related_name="albums", blank=True)
    image = models.URLField()

class Audio(models.Model):
    def __str__(self):
        return self.title + " "+str(self.id)
    name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    audioDownload = models.URLField()
    audioPlay = models.URLField()
    playCount = models.IntegerField(editable=False, default = 0)
    downloadsCount = models.IntegerField(editable=False, default = 0)
    rating = models.FloatField(editable=False, default = 0)
    numOfRatings = models.IntegerField(editable=False, default = 0)
    categories = models.ManyToManyField(Category,related_name="audios")
    uploadDate = models.DateTimeField(editable=False, default = django.utils.timezone.now)
    albums = models.ManyToManyField(Album, related_name="audios")
    artists = models.ManyToManyField(Artist, related_name="audios")

class Commentary (models.Model):
    def __str__(self):
        return self.commentary
    class Meta:
        verbose_name_plural = "commentaries"
    commentary = models.TextField()
    date = models.DateTimeField(editable=False, default=django.utils.timezone.now)
    audio = models.ForeignKey(Audio,on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, blank=True)

class Agent(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "agents"

    name = models.CharField(max_length=40)
    user = models.OneToOneField(User, null=True, blank=True)
    image = models.URLField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Artist.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.artist.save()

class Convocation(models.Model):
    def __str__(self):
        return self.title + " " + str(self.id)
    public='PUB'
    private='PRIV'
    unpublished='UP'
    published='P'
    vote='V'
    close='C'

    name = models.CharField(max_length=40)
    detail = models.CharField(max_length=5000)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    typeConvocation = ((public,'Convocatoria Publica'),(private,'Convocatoria Privada'))
    terms = models.URLField()
    dateInit = models.DateTimeField(editable=True, default=django.utils.timezone.now)
    dateEnd = models.DateTimeField(editable=True, default=django.utils.timezone.now)
    dateLimit = models.DateTimeField(editable=True, default=django.utils.timezone.now)
    dateResults = models.DateTimeField(editable=True, default=django.utils.timezone.now)
    status = ((unpublished,'Sin Publicar'),(published,'Publicada'),(vote,'En Votacion'),(close,'Cerrada'))
    winner = models.ForeignKey(Artist,on_delete=models.CASCADE,null=True,blank=True)

class ConvocationAudio(models.Model):
    convocation=models.ForeignKey(Convocation,on_delete=models.CASCADE)
    audio=models.ForeignKey(Audio,on_delete=models.CASCADE)
    votes=models.IntegerField(editable=False, default = 0)


class ConvocationVoting(models.Model):
    convocation=models.ForeignKey(Convocation,on_delete=models.CASCADE)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)


    # python manage.py makemigrations sonidosLibresApp
    # python manage.py sqlmigrate sonidosLibresApp 0001
    # python manage.py migrate
    # python manage.py createsuperuser
    # $ heroku run python manage.py migrate --app sonidoslibres