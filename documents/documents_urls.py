from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [

    url(r'^document-autocomplete/$',
        view=views.DocumentCreateAutocompleteView.as_view(),
        name='document-autocomplete'),
    url(r'^document-create/$',
        view=views.DocumentCreateFromTemplateFormView.as_view(),
        name='document-create'),
    url(r'^$',
        view=views.DocumentListView.as_view(),
        name='document-list'),
]
