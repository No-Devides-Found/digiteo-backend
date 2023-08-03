from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    # username = models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(max_length=60, unique=True, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['']  # 필수 필드로 지정

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, unique=True)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    job = models.CharField(max_length=10)
    grade = models.CharField(default="", max_length=5)
    department = models.CharField(max_length=20)
