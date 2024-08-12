from django.shortcuts import render
from . import models
# Create your views here.

def listTweet(request):
    all_tweets = models.Tweet.objects.all()
    tweetdic= {"tweets": all_tweets}
    return render(request,'tweetapp/listtweet.html')
def addTweet(request):
    
    return render(request,'tweetapp/addtweet.html')