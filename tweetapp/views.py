from django.shortcuts import render, redirect
from . import models
from django.urls import reverse,reverse_lazy
from tweetapp.forms import AddTweetForm,AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


def listTweet(request):
    all_tweets = models.Tweet.objects.all()
    tweetdic= {"tweets": all_tweets}
    return render(request,'tweetapp/listtweet.html',context=tweetdic)

@login_required(login_url="/login") # Tweet eklemek için kullanıcı giriş yapmak zorunda, giriş yapmamış ise login sayfasına yönlendirilir.
def addTweet(request):
    if request.POST:
        message = request.POST["message"]
        models.Tweet.objects.create(username=request.user,message=message)
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
@login_required    
def deletetweet(request,id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect("tweetapp:ListTweet")




class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login") #Sadece gerekli olduğu zaman reverse çalışsın diye reverse_lazy 
    template_name = "registration/signup.html"