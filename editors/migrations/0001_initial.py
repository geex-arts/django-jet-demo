# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RichTextModel',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ckeditor', ckeditor.fields.RichTextField(verbose_name='CKEditor')),
                ('tinymce', tinymce.models.HTMLField(verbose_name='TinyMCE')),
            ],
            options={
                'verbose_name': 'rich text model',
                'verbose_name_plural': 'rich text models',
            },
        ),
    ]
