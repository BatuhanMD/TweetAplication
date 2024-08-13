from django import forms

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname",max_length=50)
    message_input = forms.CharField(label="Message",max_length=255)
    