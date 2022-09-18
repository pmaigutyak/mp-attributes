
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


def setup_settings(settings, **kwargs):

    settings['INSTALLED_APPS'] += [
        app for app in [
            'ordered_model'
        ] if app not in settings['INSTALLED_APPS']
    ]


class AttributesAppConfig(AppConfig):
    name = 'attributes'
    verbose_name = _('Attributes')

default_app_config = 'attributes.AttributesAppConfig'
