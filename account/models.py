# from django.db import models
# from django.contrib.auth.models import AbstractUser, BaseUserManager
# from django.utils.crypto import get_random_string
# from slugify import slugify

# class UserManager(BaseUserManager):
#     def _create(self,phone_number, password, **exctra_fields):
#         if not phone_number:
#             raise ValueError('Не введет номер телефона')
#         if phone_number.startswitch('996'):
#             raise ValueError('Номер телефона должен начинаться с 996')
#         if len(phone_number) < 12:
#             raise ValueError('Номер должен состоять из 996 XXX-XX-XX-XX')
#         user = self.model(phone_number=phone_number, **exctra_fields)
#         user.set_password(password)
#         user.create_activation_code()
#         user.save()
#         return user
#     def create_user(self, phone_number, password, **exctra_fields):
#         return self._create(phone_number, password, **exctra_fields)
#     def create_superuser(self, phone_number, password, **exctra_fields):
#         exctra_fields.setdefault('is_staff', True)
#         exctra_fields.setdefault('is_active', True)
#         exctra_fields.setdefault('is_superuser', True)
#         return self._create(phone_number, password, **exctra_fields)
    
# class Level_User(models.Model):
#     title = models.CharField(max_length=120, unique=True, verbose_name='Должность')
#     slug = models.SlugField(max_length=120, unique=True, primary_key=True, blank=True)
#     def __str__(self):
#         return self.title
#     def save(self,*args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save()

# class User(AbstractUser):
#     phone_number = models.IntegerField(unique=True)
#     name = None
#     is_active = models.BooleanField(default=False)
#     activation_code = models.CharField(max_length=20, blank=True)
#     objects = UserManager()
#     # passport= models.ImageField(default=None)
#     # tex_passport = models.ImageField(default=None)
#     # car = models.ImageField(default=None)
#     USERNAME_FIELD = 'phone_number'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return f'{self.id} -> {self.phone_number}'
    
#     def create_activation_code(self):
#         code = get_random_string(10, allowed_chars='123456789#@!$%^&*_')
#         self.activation_code = code


from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.crypto import get_random_string
from slugify import slugify

class UserManager(BaseUserManager):
    def _create(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('Не введен номер телефона')
        if phone_number.startswith('996'):
            raise ValueError('Номер телефона должен начинаться с 996')
        if len(phone_number) < 12:
            raise ValueError('Номер должен состоять из 996 XXX-XX-XX-XX')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save()
        return user
    
    def create_user(self, phone_number, password, **extra_fields):
        return self._create(phone_number, password, **extra_fields)
    
    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create(phone_number, password, **extra_fields)
    

class Level_User(models.Model):
    title = models.CharField(max_length=120, unique=True, verbose_name='Должность')
    slug = models.SlugField(max_length=120, unique=True, primary_key=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class User(AbstractUser):
    phone_number = models.IntegerField(unique=True)
    name = None
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=20, blank=True)
    objects = UserManager()
    
    groups = None  # Add this line to override the clash with auth.User.groups
    user_permissions = None  # Add this line to override the clash with auth.User.user_permissions
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.id} -> {self.phone_number}'
    
    def create_activation_code(self):
        code = get_random_string(10, allowed_chars='123456789#@!$%^&*_')
        self.activation_code = code
