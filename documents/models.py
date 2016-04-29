from django.db import models


class DocumentType(models.Model):
    identification = models.CharField(max_length=60)
    description = models.CharField(max_length=255)

    def __str__(self):
        return '{}: {}'.format(self.identification, self.description)


class Document(models.Model):
    content = models.TextField(blank=True)
    document_type = models.ForeignKey(DocumentType, null=True, on_delete=models.SET_NULL)

    is_template = models.BooleanField(default=False)
    template_description = models.CharField(max_length=255, blank=True)
    created_from = models.ForeignKey('self', null=True, on_delete=models.SET_NULL, editable=False)

    class Meta:
        ordering = ('document_type', )
