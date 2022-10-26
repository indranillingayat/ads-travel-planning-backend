from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import validate_email

from users.manager import CustomUserManager
from users.permissions import CUSTOM_PERMISSIONS
from utils.base_model import UUIDPKAbstractModel


class User(UUIDPKAbstractModel, AbstractUser):

    username_validator = UnicodeUsernameValidator()

    username = models.EmailField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator, validate_email],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    objects = CustomUserManager()

    REQUIRED_FIELDS = []
    email = None

    class Meta:
        permissions = list(CUSTOM_PERMISSIONS.values())
