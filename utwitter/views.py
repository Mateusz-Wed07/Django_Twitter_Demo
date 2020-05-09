from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

from django.views.generic.base import TemplateView
from .models import Tweet

class FrontPage(TemplateView):
    template_name = "FrontPage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.all()
        return context

from .forms import AddTweetForm
from django.views.generic.edit import FormView
class AddTweetView(FormView):
    template_name = 'add-tweet.html'
    form_class = AddTweetForm
    def form_valid(self, form):
        new_tweet = form.instance # to jest nasz nowy tweet
        new_tweet.user = self.request.user # tu wyciągamy zalogowanego usera
        new_tweet.save() # tu zapisujemy tweeta
        return HttpResponseRedirect('/')
