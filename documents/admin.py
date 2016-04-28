from django.contrib import admin

# Register your models here.

from .models import DocumentType, Document


@admin.register(DocumentType)
class DocumentType(admin.ModelAdmin):
    list_display = ['identification', 'description']


@admin.register(Document)
class Document(admin.ModelAdmin):
    list_display = ['content', 'document_type', 'is_template', 'template_description']
