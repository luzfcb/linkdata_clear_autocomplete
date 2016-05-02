from dal import autocomplete
from django import forms

from .models import Document, DocumentType
from .widgets import ModelSelect2ForwardExtras, ModelSelect2MultipleForwardExtras


class DocumentTypeModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.identification


class DocumentTemplateModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.template_description


class DocumentTemplateModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.template_description


class DocumentCreateFromTemplateForm(forms.Form):
    document_type = DocumentTypeModelChoiceField(
        label='Document type',
        queryset=DocumentType.objects.all(),

    )
    document_template = DocumentTemplateModelChoiceField(
        label='Document Template3 - ModelSelect2 widget + ForwardExtrasMixin widget',
        queryset=Document.objects.all(),
        widget=ModelSelect2ForwardExtras(url='document-autocomplete', forward=('document_type',),
                                         unselect_if_forward_changed=['document_type', 'not_existing_field']
                                         ),
    )


class WidgetSamplesForm(forms.Form):
    document_type = DocumentTypeModelChoiceField(
        label='Document type',
        queryset=DocumentType.objects.all(),

    )
    document_template = DocumentTemplateModelChoiceField(
        label='Document Template - original ModelSelect2 widget',
        queryset=Document.objects.all(),
        widget=autocomplete.ModelSelect2(url='document-autocomplete', forward=('document_type',),
                                         ),
    )

    document_type2 = DocumentTypeModelChoiceField(
        label='Document type2',
        queryset=DocumentType.objects.all(),

    )
    document_template2 = DocumentTemplateModelMultipleChoiceField(
        label='Document Template2 - original ModelSelect2 widget',
        queryset=Document.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='document-autocomplete', forward=('document_type2',),
                                                 ),
    )

    document_type3 = DocumentTypeModelChoiceField(
        label='Document type3',
        queryset=DocumentType.objects.all(),

    )
    document_template3 = DocumentTemplateModelChoiceField(
        label='Document Template3 - ModelSelect2 widget + ForwardExtrasMixin widget',
        queryset=Document.objects.all(),
        widget=ModelSelect2ForwardExtras(url='document-autocomplete', forward=('document_type3',),
                                         unselect_if_forward_changed=('document_type3',)
                                         ),
    )

    document_type4 = DocumentTypeModelChoiceField(
        label='Document type4',
        queryset=DocumentType.objects.all(),

    )
    document_template4 = DocumentTemplateModelMultipleChoiceField(
        label='Document Template4 - ModelSelect2Multiple widget + ForwardExtrasMixin widget',
        queryset=Document.objects.all(),
        widget=ModelSelect2MultipleForwardExtras(url='document-autocomplete', forward=('document_type4',),
                                                 unselect_if_forward_changed=('document_type4',)
                                                 ),
    )
