# encoding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(_('name'), max_length=255)

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('state')
        verbose_name_plural = _('states')

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    state = models.ForeignKey(State, verbose_name=_('state'), related_name='counties')

    class Meta:
        verbose_name = _('county')
        verbose_name_plural = _('counties')
        unique_together = ('name', 'state')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''


class City(models.Model):
    name = models.CharField(_('name'), max_length=255)
    state = models.ForeignKey(State, verbose_name=_('state'), related_name='cities')
    county = models.ForeignKey(County, verbose_name=_('county'), related_name='cities')

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')
        unique_together = ('name', 'state', 'county')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ''


class Address(models.Model):
    name = models.CharField(_('name'), max_length=255)
    city = models.ForeignKey(City, verbose_name=_('city'), related_name='addresses')
    zip = models.IntegerField(_('zip/postal code'))

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')
        unique_together = ('name', 'city')

    def __str__(self):
        return self.name

    @staticmethod
    def autocomplete_search_fields():
        return 'name', 'city__name'


class Person(models.Model):
    first_name = models.CharField(_('first name'), max_length=255)
    last_name = models.CharField(_('last name'), max_length=255)
    address = models.ForeignKey(Address, verbose_name=_('address'), related_name='persons')
    company = models.ForeignKey(Company, verbose_name=_('company'), related_name='persons')
    phone = models.CharField(_('phone'), max_length=255)
    email = models.EmailField(_('email'), max_length=255)
    web = models.URLField(_('web'), max_length=255)
    # content = models.TextField(verbose_name=u'Содержание')
    # visible_for_unauthorized = models.BooleanField(default=True, verbose_name=u'Видна для неавторизованных')
    # visible_for_authorized = models.BooleanField(default=True, verbose_name=u'Видна для авторизованных')

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('persons')
        # ordering = ('url',)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
