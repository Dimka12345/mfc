# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.template.context_processors import csrf, request
#from mfc.models import User

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/main')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/main')

def register(request):
    return render(request, 'loginsys/register.html')


