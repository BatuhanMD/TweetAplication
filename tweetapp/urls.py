from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('',views.listTweet,name ="İndex"),
    path('listtweet/', views.listTweet,name='ListTweet'),
    path('addtweet/', views.addTweet,name='AddTweet'),
    path('addtweetform/', views.addTweetForm,name='AddTweetForm'),
    path('addtweetmodelform/', views.addTweetModelForm,name='AddTweetModelForm'),
]