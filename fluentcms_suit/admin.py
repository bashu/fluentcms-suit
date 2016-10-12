# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class SuitAdminMixin(object):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if 'suit' in settings.INSTALLED_APPS:
            from suit.widgets import SuitSplitDateTimeWidget, SuitDateWidget

            if isinstance(db_field, models.DateTimeField):
                kwargs.setdefault('widget', SuitSplitDateTimeWidget)
            elif isinstance(db_field, models.DateField):
                kwargs.setdefault('widget', SuitDateWidget)
        return super(SuitAdminMixin, self).formfield_for_dbfield(db_field, **kwargs)
