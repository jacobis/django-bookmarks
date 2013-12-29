# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import logout
from django.contrib.auth.models import User

import settings

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def main_page(request):
    print settings.STATIC_ROOT
    return render_to_response(
        'main_page.html',
        {'user': request.user}
    )

def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('사용자를 찾을 수 없습니다.')

    bookmarks = user.bookmark_set.all()

    template = get_template('user_page.html')
    variables = Context({
        'username': username,
        'bookmarks': bookmarks
        })
    output = template.render(variables)
    return HttpResponse(output)