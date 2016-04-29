from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$',
        view=views.DocumentListView.as_view(),
        name='document-list'),

    url(r'^document-autocomplete/$',
        view=views.DocumentCreateAutocompleteView.as_view(),
        name='document-autocomplete'),
    url(r'^document-create/$',
        view=views.DocumentCreateFromTemplateFormView.as_view(),
        name='document-create'),
    url(r'^document-edit/(?P<pk>\d+)/$',
        view=views.DocumentEditView.as_view(),
        name='document-edit'),

]
