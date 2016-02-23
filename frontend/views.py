# -*- coding: utf-8 -*-
import urllib2

from django.views.generic import View, ListView
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse

from bs4 import BeautifulSoup
from beautifulsoupselect.soupselect import select

from .models import Post


class UpdateBase(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        url = 'http://bash.im'
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib2.Request(url, None, headers)
        soup = BeautifulSoup(urllib2.urlopen(req))
        quotes = soup.find_all('div', class_='quote')
        for div_quote in quotes:
            text_div = select(div_quote, 'div.text')
            post_id = select(div_quote, 'div.actions a.id')

            try:
                post_id[0]
            except:
                continue

            post_id = post_id[0].text.replace('#', '')
            post_text = text_div[0].text

            try:
                Post.objects.get(bash_id=post_id)
            except Post.DoesNotExist:
                Post.objects.create(
                    bash_id=int(post_id),
                    text=post_text
                )

        return HttpResponseRedirect(reverse('home'))


class Homepage(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
