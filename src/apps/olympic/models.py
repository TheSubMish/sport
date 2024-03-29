from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CountryChoices(models.TextChoices):
    NEPAL = 'nepal','Nepal'
    INDIA = 'india','India'
    CHINA = 'china','China'
    AMERICA = 'america','America'
    AUSTRALIA = 'australia','Australia'
    CANADA = 'canada','Canada'


# Create your models here.
class Sport(models.Model):

    name = models.CharField(max_length=255,null=False,blank=False)
    featured_image = models.ImageField(upload_to='Images/')
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class GameHighlight(models.Model):
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=False,blank=False)
    video = models.FileField(upload_to='video/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(username, email, first_name=first_name, last_name=last_name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    country = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        choices=CountryChoices.choices,
        default=CountryChoices.NEPAL
    )

    fav_sport = models.CharField(max_length=255,null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str__(self):
        return self.username