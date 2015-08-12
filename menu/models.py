# encoding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


@python_2_unicode_compatible
class MenuItemCategory(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    order = models.PositiveIntegerField(_('order'), default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('order',)
        verbose_name = _('menu item category')
        verbose_name_plural = _('menu item categories')

    def __str__(self):
        return self.title


class MenuItem(MPTTModel):
    name = models.CharField(_('name'), max_length=50, unique=True)
    parent = TreeForeignKey('self', verbose_name=_('parent menu item'),
                            null=True, blank=True, related_name='children', db_index=True)
    order = models.PositiveIntegerField(_('order'), default=0, blank=False, null=False)
    category = models.ForeignKey(MenuItemCategory, verbose_name=_('category'))

    class Meta(object):
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')
        ordering = ('order',)

    class MPTTMeta:
        order_insertion_by = ('name',)

    def __str__(self):
        return self.name



