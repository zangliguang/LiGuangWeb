from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BaseServiceConfig(AppConfig):
    name = 'BaseService'
    verbose_name = _("BaseService")
    verbose_name_plural = _("BaseService List")
