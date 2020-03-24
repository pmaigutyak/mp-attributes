
from django.conf import settings

from attributes import defaults


ATTRIBUTES_CATEGORY_MODEL = getattr(
    settings, 'ATTRIBUTES_CATEGORY_MODEL', defaults.ATTRIBUTES_CATEGORY_MODEL)

ATTRIBUTES_ENTRY_MODEL = getattr(
    settings, 'ATTRIBUTES_ENTRY_MODEL', defaults.ATTRIBUTES_ENTRY_MODEL)
