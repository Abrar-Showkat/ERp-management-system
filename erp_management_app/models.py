from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_delete, pre_delete, pre_save

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, email, name, phone, is_admin, password=None):
        if not email:
            ValueError('User must provide an email')
        user = self.model(username=username, email=email, firstname=firstname,
                          lastname=lastname, phone=phone, is_admin=True)
        user.set_password(password)
        user.save(using=self._db)

        return user

#  for user to add custom roles


class Roles(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(AbstractBaseUser):

    INDIA = 'IND'
    PAKISTAN = 'PAK'
    BANGLADESH = 'BAN'
    CHINA = 'CH'
    USA = 'US'
   # temporary list of countries for this assignment else use django_countries for production based project
    COUNTRIES = [
        (INDIA, 'India'),
        (PAKISTAN, 'Pakistan'),
        (BANGLADESH, 'Bangladesh'),
        (CHINA, 'China'),
        (USA, 'Usa'),
    ]

    email = models.EmailField(max_length=30, unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=500)
    password2 = models.CharField(max_length=30)
    phone = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=3, choices=COUNTRIES, default=INDIA)
    business_name = models.CharField(max_length=20)
    role = models.OneToOneField(Roles, on_delete=models.CASCADE, default=1)
    otp_counter = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=True,)
    is_staff = models.BooleanField(default=True)

    last_login = None

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    User = models.Manager()

    def __str__(self):
        return self.name

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value


#


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=300)
    password2 = models.CharField(max_length=30)
    phone = models.IntegerField(blank=True, null=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, default=2)
    otp_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name
