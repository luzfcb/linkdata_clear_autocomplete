from dal import autocomplete
from django import forms

from .models import Document, DocumentType


class DocumentTypeModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.identification


class DocumentTemplateModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.template_description


class DocumentCreateFromTemplateForm(forms.Form):
    document_type = DocumentTypeModelChoiceField(
        label='Document type',
        queryset=DocumentType.objects.all(),

    )
    document_template = DocumentTemplateModelChoiceField(
        label='Document Template',
        queryset=Document.objects.all(),
        widget=autocomplete.ModelSelect2(url='document-autocomplete', forward=('document_type',)),
    )
