from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import validate_email

from users.manager import CustomUserManager
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
        permissions = [
            ('c_create_trip', 'Can create new trip'),
            ('c_list_trip', 'Can list the created trips'),
            ('c_manage_team', 'Can manage team trips'),
            ('c_participated_trips', 'Can view participated trips'),
            ('c_create_trip_request', 'Can create trip requests'),
            ('c_manage_trip_request', 'Can manage trip requests'),
            ('c_access_ads_shared_trips', 'Can view all the shared with ADS trips'),
            ('c_access_external_shared_trips', 'Can view all the trips shared externally')
        ]
