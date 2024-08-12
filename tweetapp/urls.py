from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('listtweet/', views.listTweet,name='ListTweet'),
    path('addtweet/', views.addTweet,name='AddTweet'),
]