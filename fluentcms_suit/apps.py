# -*- coding: utf-8 -*-

from django.conf import settings
from django.apps import AppConfig


class DefaultConfig(AppConfig):
    label = name = 'fluentcms_suit'

    def ready(self):
        try:
            if 'fluent_pages' in settings.INSTALLED_APPS:
                from fluent_pages.extensions import page_type_pool
                from fluent_contents.extensions import plugin_pool

                from .admin import SuitAdminMixin

                for p in page_type_pool.get_plugins():
                    class PageTypeAdmin(SuitAdminMixin, p.model_admin):
                        pass
                    p.model_admin = PageTypeAdmin

                for p in plugin_pool.get_plugins():
                    try:
                        class PluginAdmin(SuitAdminMixin, p.model_admin):
                            pass

                        p.model_admin = PluginAdmin
                    except AttributeError:
                        pass

        except:
            pass  # shit happens
