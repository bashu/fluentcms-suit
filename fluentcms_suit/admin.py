from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class SuitAdminMixin:
    def formfield_for_dbfield(self, db_field, **kwargs):
        if "suit" in settings.INSTALLED_APPS:
            from suit.widgets import SuitDateWidget, SuitSplitDateTimeWidget

            if isinstance(db_field, models.DateTimeField):
                kwargs.setdefault("widget", SuitSplitDateTimeWidget)
            elif isinstance(db_field, models.DateField):
                kwargs.setdefault("widget", SuitDateWidget)
        return super().formfield_for_dbfield(db_field, **kwargs)


class FluentPagesParentAdminMixin:
    def get_action_icons(self, node):
        actions = []
        if node.can_have_children:
            actions.append(
                """<a href="add/?{parent_attr}={id}" title="{title}" class="add-child-object"><i class="icon-plus-sign icon-alpha75"></i></a>""".format(
                    parent_attr=self.model._mptt_meta.parent_attr,
                    id=node.pk,
                    title=_("Add sub node"),
                    static=settings.STATIC_URL,
                )
            )
        else:
            actions.append(self.EMPTY_ACTION_ICON.format(STATIC_URL=settings.STATIC_URL, css_class="add-child-object"))

        if self.can_preview_object(node):
            actions.append(
                """<a href="{url}" title="{title}" target="_blank" class="viewsitelink"><i class="icon-globe icon-alpha75"></i></a>""".format(
                    url=node.get_absolute_url(), title=_("View on site"), static=settings.STATIC_URL
                )
            )

        # The is_first_sibling and is_last_sibling is quite heavy. Instead rely on CSS to hide the arrows.
        move_up = f'<a href="{node.pk}/move_up/" class="move-up">\u2191</a>'
        move_down = f'<a href="{node.pk}/move_down/" class="move-down">\u2193</a>'
        actions.append(f'<span class="no-js">{move_up}{move_down}</span>')
        return actions
