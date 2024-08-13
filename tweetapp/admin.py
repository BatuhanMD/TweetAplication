from django.contrib import admin
from tweetapp.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nickname Group:',{"fields":["nickname"]}),
        ('Message Group:',{"fields":["message"]})
    ]
admin.site.register(Tweet,TweetAdmin)

