import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


class User(models.Model):
    displayName = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100, null=False, default='')

    def get_user_email(self):
        return self.email

    def get_user_name(self):
        return self.displayName

    def __str__(self):
        return self.id

# import uuid
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


# class User(AbstractBaseUser, PermissionsMixin):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     displayName = models.CharField(max_length=50, default='')
#     email = models.EmailField(max_length=100, unique=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return str(self.id)

#     def get_user_email(self):
#         return self.email

#     def get_user_name(self):
#         return self.displayName
