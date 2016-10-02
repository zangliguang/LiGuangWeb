from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BaseServiceConfig(AppConfig):
    name = 'baseservice'
    verbose_name = _("baseservice")
    verbose_name_plural = _("baseservice List")
