# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class SuitAdminMixin(object):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if 'suit' in settings.INSTALLED_APPS:
            from suit.widgets import SuitSplitDateTimeWidget, SuitDateWidget

            if isinstance(db_field, models.DateTimeField):
                kwargs.setdefault('widget', SuitSplitDateTimeWidget)
            elif isinstance(db_field, models.DateField):
                kwargs.setdefault('widget', SuitDateWidget)
        return super(SuitAdminMixin, self).formfield_for_dbfield(db_field, **kwargs)

    
class FluentPagesParentAdminMixin(object):

    def get_action_icons(self, node):
        actions = []
        if node.can_have_children:
            actions.append(
                """<a href="add/?{parent_attr}={id}" title="{title}" class="add-child-object"><i class="icon-plus-sign icon-alpha75"></i></a>""".format(parent_attr=self.model._mptt_meta.parent_attr, id=node.pk, title=_('Add sub node'), static=settings.STATIC_URL))
        else:
            actions.append(self.EMPTY_ACTION_ICON.format(STATIC_URL=settings.STATIC_URL, css_class='add-child-object'))

        if self.can_preview_object(node):
            actions.append(
                """<a href="{url}" title="{title}" target="_blank" class="viewsitelink"><i class="icon-globe icon-alpha75"></i></a>""".format(url=node.get_absolute_url(), title=_('View on site'), static=settings.STATIC_URL))

        # The is_first_sibling and is_last_sibling is quite heavy. Instead rely on CSS to hide the arrows.
        move_up = u'<a href="{0}/move_up/" class="move-up">\u2191</a>'.format(node.pk)
        move_down = u'<a href="{0}/move_down/" class="move-down">\u2193</a>'.format(node.pk)
        actions.append(u'<span class="no-js">{0}{1}</span>'.format(move_up, move_down))
        return actions
