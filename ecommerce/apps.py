from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class EcommerceConfig(AppConfig):
    name = "ecommerce"
    verbose_name = _("Ecommerce")
    verbose_name_plural = _("Ecommerce List")