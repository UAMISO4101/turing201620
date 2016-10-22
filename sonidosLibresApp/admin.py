from django.contrib import admin

from .models import Category, Audio, Commentary, Album, Artist,Convocation,ConvocationAudio,ConvocationVoting,Agent

admin.site.register(Category)
admin.site.register(Audio)
admin.site.register(Commentary)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(ConvocationVoting)
admin.site.register(Convocation)
admin.site.register(ConvocationAudio)
admin.site.register(Agent)