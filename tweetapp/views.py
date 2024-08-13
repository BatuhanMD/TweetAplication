from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from tweetapp.forms import AddTweetForm,AddTweetModelForm

def listTweet(request):
    all_tweets = models.Tweet.objects.all()
    tweetdic= {"tweets": all_tweets}
    return render(request,'tweetapp/listtweet.html',context=tweetdic)
def addTweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nickname,message=message)
        return redirect(reverse('tweetapp:ListTweet'))
    return render(request,'tweetapp/addtweet.html')

def addTweetForm(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('tweetapp:ListTweet'))
    else: 
        form = AddTweetForm()
        return render(request,'tweetapp/addtweetform.html',context={"Form":form})
    
def addTweetModelForm(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('tweetapp:ListTweet'))
    else: 
        form = AddTweetModelForm()
        return render(request,'tweetapp/addtweetmodelform.html',context={"Form":form})
   
    