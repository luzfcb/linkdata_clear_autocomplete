from dal import autocomplete
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import never_cache

from .models import Document
from .forms import DocumentCreateFromTemplateForm


class DocumentCreateAutocompleteView(autocomplete.Select2QuerySetView):
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(DocumentCreateAutocompleteView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # if not self.request.user.is_authenticated():
        #     return Document.objects.none()

        document_type = self.forwarded.get('document_type', None)

        qs = Document.objects.filter(is_template=True)

        if document_type:
            qs = qs.filter(document_type_id=document_type)
            if self.q:
                qs = qs.filter(template_description__icontains=self.q)

        else:
            qs = Document.objects.none()

        return qs

    def get_result_label(self, result):
        return result.template_description


class DocumentCreateFromTemplateFormView(generic.FormView):
    template_name = 'document/create_from_template.html'
    form_class = DocumentCreateFromTemplateForm

    def form_valid(self, form):
        document_template = form.cleaned_data['document_template']

        document_kwargs = {
            'content': 'created from template "{}"'.format(document_template.content),
            'document_type': document_template.document_type,
            'is_template': False,
            'template_description': '',
            'created_from': document_template
        }

        new_document = Document(**document_kwargs)
        new_document.save()

        return redirect(reverse('document-list'))


class DocumentListView(generic.ListView):
    model = Document
    template_name = 'document/list.html'

    def get_context_data(self, **kwargs):
        context = super(DocumentListView, self).get_context_data(**kwargs)
        object_list = context.get('object_list', None)
        context['object_list_is_template'] = object_list.filter(is_template=True)
        context['object_list_not_is_template'] = object_list.filter(is_template=False)
        return context


class DocumentEditView(generic.UpdateView):
    model = Document
    fields = '__all__'
    template_name = 'document/edit.html'
    success_url = reverse_lazy('document-list')