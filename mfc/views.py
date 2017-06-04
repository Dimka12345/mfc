from datetime import timezone, datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib import auth
from django.template import RequestContext
from django.template.context_processors import csrf

from MyMFC import settings
from mfc.models import New, Passport, Service, Document, Request, Image, PersonalInfo
from mfc.forms import Passport_Editing_Form, Order_Service_Form, Add_Document_Form, Document_Rename_Form, Document_Delete_Form, Personal_Info_Form


def main(request):
    news_latest = New.objects.order_by('-time_of_publishing')[:3]
    context_latest_news = {
        'news_latest':news_latest,
        'username': auth.get_user(request).username
    }
    return render_to_response('mfc/main.html', context_latest_news)

def news(request):
    news = New.objects.order_by('-time_of_publishing')
    context = {
        'news':news,
        'username': auth.get_user(request).username
    }
    return render(request, 'mfc/news.html', context)

def one_new(request, new_id):
    new = get_object_or_404(New, id=new_id)
    username = auth.get_user(request).username
    return render_to_response('mfc/one_new.html', {'new': new, 'username': username})

def rename_document(request, document_id):
    user = auth.get_user(request).username
    if user:
        username = auth.get_user(request).username
        document = get_object_or_404(Document, id=document_id)
        document_1 = document
        if request.method == "POST":
            form__ = Document_Rename_Form(request.POST, instance=document)
            if form__.is_valid():
                document = form__.save(commit=False)
                document.login = request.user  # auth.get_user(request).id
                document.picture = document_1.picture
                document.save()
                return redirect('/cabinet')
        else:
            form__ = Document_Rename_Form(instance=document)
        return render(request, 'mfc/rename_document.html', {'form__': form__, 'username': username, 'document': document})
    else:
        return render(request, 'login.html')

def delete_document(request, document_id):
    user = auth.get_user(request).username
    if user:
        username = auth.get_user(request).username
        document = get_object_or_404(Document, id=document_id)
        document.delete()
        try:
            Passport.objects.get(login=auth.get_user(request).id)
            context = {
                'username': auth.get_user(request).username,
                'passport': Passport.objects.get(login=auth.get_user(request).id),
                'document': Document.objects.filter(login=auth.get_user(request).id),
                'request': Request.objects.filter(login=auth.get_user(request).id),
            }
        except Passport.DoesNotExist:
            context = {
                'username': auth.get_user(request).username,
                'passport': Passport.objects.filter(login=auth.get_user(request).id),
                'document': Document.objects.filter(login=auth.get_user(request).id),
                'request': Request.objects.filter(login=auth.get_user(request).id),
            }
        return render_to_response('mfc/cabinet.html', context)
    else:
        return render(request, 'login.html')


def cabinet(request):
    user = auth.get_user(request).username
    if user:
        if request.method == "POST":
            form = Add_Document_Form(request.POST, request.FILES)
            if form.is_valid():
                document_add = form.save(commit=False)
                document_add.login = request.user
                document_add.save()
        else:
            form = Add_Document_Form()
        try:
            Passport.objects.get(login=auth.get_user(request).id)
            try:
                PersonalInfo.objects.get(login=auth.get_user(request).id)
                context = {
                    'username': auth.get_user(request).username,
                    'email': auth.get_user(request).email,
                    'personal_info': PersonalInfo.objects.get(login=auth.get_user(request).id),
                    'passport': Passport.objects.get(login=auth.get_user(request).id),
                    'document': Document.objects.filter(login=auth.get_user(request).id).order_by('-date_of_adding'),
                    'request_all': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning'),
                    'request_last': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning')[:5],
                    'request_start': Request.objects.filter(login=auth.get_user(request).id, status='подана').order_by('-date_of_beginning'),
                    'request_in_progress': Request.objects.filter(login=auth.get_user(request).id, status='обрабатывается').order_by('-date_of_beginning'),
                    'request_ending': Request.objects.filter(login=auth.get_user(request).id, status='завершена').order_by('-date_of_beginning'),
                    'form': form
                }
            except PersonalInfo.DoesNotExist:
                context = {
                    'username': auth.get_user(request).username,
                    'email': auth.get_user(request).email,
                    'personal_info': PersonalInfo.objects.filter(login=auth.get_user(request).id),
                    'passport': Passport.objects.get(login=auth.get_user(request).id),
                    'document': Document.objects.filter(login=auth.get_user(request).id).order_by('-date_of_adding'),
                    'request_all': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning'),
                    'request_last': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning')[:5],
                    'request_start': Request.objects.filter(login=auth.get_user(request).id, status='подана').order_by('-date_of_beginning'),
                    'request_in_progress': Request.objects.filter(login=auth.get_user(request).id, status='обрабатывается').order_by('-date_of_beginning'),
                    'request_ending': Request.objects.filter(login=auth.get_user(request).id, status='завершена').order_by('-date_of_beginning'),
                    'form': form
                }
        except Passport.DoesNotExist:
            try:
                PersonalInfo.objects.get(login=auth.get_user(request).id)
                context = {
                    'username': auth.get_user(request).username,
                    'email': auth.get_user(request).email,
                    'personal_info': PersonalInfo.objects.get(login=auth.get_user(request).id),
                    'passport': Passport.objects.filter(login=auth.get_user(request).id),
                    'document': Document.objects.filter(login=auth.get_user(request).id).order_by('-date_of_adding'),
                    'request_all': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning'),
                    'request_last': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning')[:5],
                    'request_start': Request.objects.filter(login=auth.get_user(request).id, status='подана').order_by('-date_of_beginning'),
                    'request_in_progress': Request.objects.filter(login=auth.get_user(request).id, status='обрабатывается').order_by('-date_of_beginning'),
                    'request_ending': Request.objects.filter(login=auth.get_user(request).id, status='завершена').order_by('-date_of_beginning'),
                    'form': form
                }
            except PersonalInfo.DoesNotExist:
                context = {
                    'username': auth.get_user(request).username,
                    'email': auth.get_user(request).email,
                    'personal_info': PersonalInfo.objects.filter(login=auth.get_user(request).id),
                    'passport': Passport.objects.filter(login=auth.get_user(request).id),
                    'document': Document.objects.filter(login=auth.get_user(request).id).order_by('-date_of_adding'),
                    'request_all': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning'),
                    'request_last': Request.objects.filter(login=auth.get_user(request).id).order_by('-date_of_beginning')[:5],
                    'request_start': Request.objects.filter(login=auth.get_user(request).id, status='подана').order_by('-date_of_beginning'),
                    'request_in_progress': Request.objects.filter(login=auth.get_user(request).id, status='обрабатывается').order_by('-date_of_beginning'),
                    'request_ending': Request.objects.filter(login=auth.get_user(request).id, status='завершена').order_by('-date_of_beginning'),
                    'form': form
                }
        return render(request, 'mfc/cabinet.html', context)
    else:
        return render(request, 'login.html')

def requests(request):
    user = auth.get_user(request).username
    if user:
        context_requests = {
            'request':Request.objects.filter(login=auth.get_user(request).id),
            'document': Document.objects.filter(login=auth.get_user(request).id),
            'username':auth.get_user(request).username
        }
        return render_to_response('mfc/requests.html', context_requests)
    else:
        return render(request, 'login.html')

def description_request(request, request_id):
    user = auth.get_user(request).username
    if user:
        request_ = get_object_or_404(Request, id=request_id)
        document = Document.objects.filter(login=auth.get_user(request).id),
        username = auth.get_user(request).username
        return render_to_response('mfc/description_request.html', {'request': request_, 'username': username, 'document': document})
    else:
        return render(request, 'login.html')

def editing_passport(request):
    user = auth.get_user(request).username
    if user:
        try:
            PersonalInfo.objects.get(login=auth.get_user(request).id)
            personal_info = PersonalInfo.objects.get(login=auth.get_user(request).id)
            email = auth.get_user(request).email,
            if request.method == "POST":
                form_ = Personal_Info_Form(request.POST, instance=personal_info)
                form_.post = email
                if form_.is_valid():
                    personal_info = form_.save(commit=False)
                    personal_info.login = request.user
                    personal_info.save()
                    return redirect('/cabinet')
            else:
                form_ = Personal_Info_Form(instance=personal_info)
        except PersonalInfo.DoesNotExist:
            email = auth.get_user(request).email,
            if request.method == "POST":
                form_ = Personal_Info_Form(request.POST)
                form_.post = email
                if form_.is_valid():
                    personal_info = form_.save(commit=False)
                    user.email = personal_info.post
                    personal_info.login = request.user
                    personal_info.save()
                    return redirect('/cabinet')
            else:
                form_ = Personal_Info_Form()
        try:
            Passport.objects.get(login=auth.get_user(request).id),
            passport = Passport.objects.get(login=auth.get_user(request).id)
            if request.method == "POST":
                form = Passport_Editing_Form(request.POST, instance=passport)
                if form.is_valid():
                    passport = form.save(commit=False)
                    passport.login = request.user
                    passport.save()
                    return redirect('/cabinet')
            else:
                form = Passport_Editing_Form(instance=passport)
        except Passport.DoesNotExist:
            if request.method == "POST":
                form = Passport_Editing_Form(request.POST)
                if form.is_valid():
                    passport = form.save(commit=False)
                    passport.login = request.user
                    passport.save()
                    return redirect('/cabinet')
            else:
                form = Passport_Editing_Form()
        context = {
            'username': auth.get_user(request).username,
            'form': form,
            'form_': form_
        }
        return render(request, 'mfc/editing_passport.html', context)
    else:
        return render(request, 'login.html')


def add_passport_request(request):
    user = auth.get_user(request).username
    if user:
        username = auth.get_user(request).username
        if request.method == "POST":
            form = Passport_Editing_Form(request.POST)
            if form.is_valid():
                passport = form.save(commit=False)
                passport.login = request.user  # auth.get_user(request).id
                passport.save()
                return redirect('/services')
        else:
            form = Passport_Editing_Form()
        return render(request, 'mfc/add_passport_request.html', {'form': form, 'username': username})
    else:
        return render(request, 'login.html')

def services(request):
    context_services = {
        'service': Service.objects.all(),
        'username': auth.get_user(request).username,
        'passport': Passport.objects.filter(login=auth.get_user(request).id)
    }
    return render(request, 'mfc/services.html', context_services)

def order_service(request, service_id):
    user = auth.get_user(request).username
    if user:
        username = auth.get_user(request).username
        service = get_object_or_404(Service, id=service_id)
        document = Document.objects.filter(login=auth.get_user(request).id)
        if request.method == "POST":
            form = Order_Service_Form(request.POST, document)
            if form.is_valid():
                request_ = form.save(commit=False)
                request_.title = service.title
                request_.service_fk = service
                request_.login = request.user
                request_.date_of_beginning = datetime.now()
                request_.date_of_ending = datetime.now()
                request_.save()
                form = Order_Service_Form()
        else:
            form = Order_Service_Form()
        passport = Passport.objects.get(login=auth.get_user(request).id)
        if request.method == "POST":
            form_ = Add_Document_Form(request.POST, request.FILES)
            if form_.is_valid():
                document_ = form_.save(commit=False)
                document_.login = request.user
                document_.save()
                return render(request, 'mfc/order_service.html', {'service': service, 'username': username,
                                                      'document': document, 'passport': passport, 'form_': form_, 'form': form})
        else:
            form_ = Add_Document_Form()
        return render(request, 'mfc/order_service.html', {'service': service, 'username': username, 'passport': passport, 'form_':form_, 'form': form,
                                                      'document': document})
    else:
        return render(request, 'login.html')

def contacts(request):
    context = {
        'username':auth.get_user(request).username
    }
    return render(request, 'mfc/contacts.html', context)

def tasks(request):
    context = {
        'username': auth.get_user(request).username
    }
    return render(request, 'mfc/tasks.html', context)

def regulations(request):
    context = {
        'username': auth.get_user(request).username
    }
    return render(request, 'mfc/regulations.html', context)

def instructions(request):
    context = {
        'username':auth.get_user(request).username
    }
    return render(request, 'mfc/instructions.html', context)