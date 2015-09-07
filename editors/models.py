# encoding: utf-8
from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField


class RichTextModel(models.Model):
    ckeditor = RichTextField('CKEditor')
    tinymce = HTMLField('TinyMCE')

    class Meta:
        verbose_name = _('rich text model')
        verbose_name_plural = _('rich text models')

    def __str__(self):
        return 'Rich text editors example'
