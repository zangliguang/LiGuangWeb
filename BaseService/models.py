import uuid
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django.core import validators


# Create your models here.
class common_user(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    phone = models.CharField(_('phone number'), max_length=20, blank=True)
    portrait_url=models.URLField(_('portrait'), default='http://img5.imgtn.bdimg.com/it/u=4069668134,267237781&fm=21&gp=0.jpg',blank=True)

    class Meta:
        verbose_name = _("basic user")
        verbose_name_plural = _("basic user list")