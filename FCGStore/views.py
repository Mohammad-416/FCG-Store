from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template import loader
import os
from .models import Game
import math


# Create your views here.
def index(request):
    index_template = loader.get_template('index.html')
    content = Game.objects.all().order_by('-id').values()
    n = 0
    data = []
    for i in content:
        len = i['id'] + n
        if i['id'] >= len - 2:
            data.append(i)
            n += 1
        else:
            break

    data.reverse()

    n = 0
    sidebar_data = []
    for i in content:
        len = i['id'] + n
        if i['id'] >= len - 3:
            sidebar_data.append(i)
            n += 1
        else:
            break
    context = {'data': data, 'sidebar_data': sidebar_data}
    return HttpResponse(index_template.render(context, request))


def blog(request, num):

    blog_template = loader.get_template('blog.html')
    content = Game.objects.all().order_by('-id').values()

    n = 0
    sidebar_data = []
    for i in content:
        len = i['id'] + n
        if i['id'] >= len - 3:
            sidebar_data.append(i)
            n += 1
        else:
            break

    data = list(content)
    length = 0
    for i in data:
        length += 1
    length = math.ceil(length / 3)
    data_chunks = data[(num - 1) * 3:num * 3]
    prenum = num - 1
    postnum = num + 1
    number = num

    context = {
        'data': data,
        'sidebar_data': sidebar_data,
        'data_chunks': data_chunks,
        'length': length,
        'number': number,
        'prenum': prenum,
        'postnum': postnum
    }

    return HttpResponse(blog_template.render(context, request))


def contact(request):
    contact_template = loader.get_template('contact.html')
    return HttpResponse(contact_template.render())


def game_single(request):
    game_single_template = loader.get_template('game-single.html')
    return HttpResponse(game_single_template.render())


def games(request):
    games_template = loader.get_template('games.html')
    return HttpResponse(games_template.render())


def review(request):
    review_template = loader.get_template('review.html')
    return HttpResponse(review_template.render())
