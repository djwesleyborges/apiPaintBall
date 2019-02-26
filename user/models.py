import jwt
from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

from perfil.models import Perfil


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)  # Criptografa a senha do usuario
        # user.save(using=self._db) # para setar em qual banco sera consultado
        user.save()

        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    username = None
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    # @property
    # def token(self):
    #     return self._generate_jwt_token()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    # def _generate_jwt_token(self):
    #     dt = datetime.now() + timedelta(days=60)
    #
    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': int(dt.strftime('%s'))
    #     }, settings.SECRET_KEY, algorithm='HS256')
    #
    #     return token.decode('utf-8')
