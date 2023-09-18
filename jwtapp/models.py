from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.utils import timezone


# Create your models here.


class UserAccountManager(BaseUserManager):
    def _create_user(
        self, mobile, password=None, confirm_password=None, **extra_fields
    ):
        user = self.model(mobile=mobile, **extra_fields)

        if password:
            user.set_password(password)
        user.save()
        return user

    def create_user(self, mobile, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(mobile, **extra_fields)

    def create_admin(self, mobile, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(mobile, password, **extra_fields)

    def create_superuser(self, mobile, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(mobile, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email address"),unique=True)
    mobile = models.CharField(_("Mobile"), max_length=20, unique=True)
    state = models.CharField(_("State"), max_length=100, blank=True, null=True)
    
    postal_pincode = models.IntegerField(_("Postal Pin Code"), blank=True, null=True)
    ragistration_date = models.DateTimeField(
        _("Date of registration"), default=timezone.now
    )
    valid_upto = models.DateTimeField(_("Date of Expire"), null=True, blank=True)
    expired = models.BooleanField(default=False)
   
    is_superuser = models.BooleanField(
        _("Superuser"),
        default=False,
        help_text=_("Designates whether this user should be treated as SuperUser."),
    )
    is_staff = models.BooleanField(
        _("Company Admin"),
        default=False,
        help_text=_("Designates whether the user is a company admin or not."),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=False,
        help_text=_("Designates whether this user should be treated as active."),
    )

    objects = UserAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-pk"]

    def __str__(self):
        return self.email






class Student(models.Model):
    email = models.EmailField(_("Email address"))
    mobile = models.CharField(_("Mobile"), max_length=20, unique=True)
    state = models.CharField(_("State"), max_length=100, blank=True, null=True)
    schoolname = models.CharField(
        _("School Name"), max_length=100, blank=True, null=True
    )