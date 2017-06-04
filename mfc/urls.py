from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^main', views.main, name='main'),
    url(r'^news', views.news, name='news'),
    url(r'^cabinet', views.cabinet, name='cabinet'),
    url(r'^editing_passport', views.editing_passport, name='editing_passport'),
    url(r'^services', views.services, name='services'),
    url(r'^order_service/(?P<service_id>[0-9]+)/$', views.order_service, name='order_service'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^add_passport_request', views.add_passport_request, name='add_passport_request'),
    url(r'^one_new/(?P<new_id>[0-9]+)/$', views.one_new, name='one_new'),
    url(r'^description_request/(?P<request_id>[0-9]+)/$', views.description_request, name='description_request'),
    url(r'^rename_document/(?P<document_id>[0-9]+)/$', views.rename_document, name='rename_document'),
    url(r'^delete_document/(?P<document_id>[0-9]+)/$', views.delete_document, name='delete_document'),
    url(r'^tasks', views.tasks, name='tasks'),
    url(r'^regulations', views.regulations, name='regulations'),
    url(r'^instructions', views.instructions, name='instructions')
]
