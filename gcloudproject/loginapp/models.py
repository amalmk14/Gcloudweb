from django.db import models
from allauth.socialaccount.models import SocialAccount
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        if not phone:
            raise ValueError('The Phone Number must be set')

        user = self.model(
            username=username,
            phone=phone,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

     

    def create_superuser(self, username, phone,email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, phone,email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    cuid = models.IntegerField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=50,unique=True)
    # password = models.TextField()
    email = models.EmailField()
    phone = models.TextField(default='123 123 1235',blank=True)
    country = models.CharField(max_length=100,blank=True)
    # cuid = models.CharField(max_length=10, unique=True)
    is_verified = models.BooleanField(default=False)
    delete_token = models.TextField()
    
    registered_date = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'phone','email']

    objects = CustomUserManager()

    def _str_(self):
        return self.username
    
    # def save(self, *args, **kwargs):
    #     if not self.cuid:
    #         last_cuid = CustomUser.objects.aggregate(models.Max('cuid'))['cuid__max'] or 99999
    #         self.cuid = last_cuid + 1
    #     super().save(*args, **kwargs)
    def save(self, *args, **kwargs):
        # # Ensure unique cuid
        # if not self.cuid:
        #     last_cuid = CustomUser.objects.aggregate(models.Max('cuid'))['cuid__max'] or 99999
        #     self.cuid = last_cuid + 1
        if not self.cuid:
            last_cuid = CustomUser.objects.aggregate(models.Max('cuid'))['cuid__max'] or 99999
            self.cuid = last_cuid + 1
        super().save(*args, **kwargs)  # Save the CustomUser instance first
        
       # Check if the user is created from a social account
        is_social_login = False
        if self.pk is not None:  # Ensure that the CustomUser instance has been saved
            try:
                social_account = self.socialaccount_set.get()
                is_social_login = True
            except SocialAccount.DoesNotExist:
                pass
        
        # If the user is created from a social account and is not verified yet
        if is_social_login and not self.is_verified:
            self.is_verified = True
            self.save(update_fields=['is_verified'])  # Save only the is_verified field

    class Meta:
       permissions = [
            ('can_view_customuser', 'Can view custom users'),
            ('can_change_customuser', 'Can change custom users'),
            ('can_delete_customuser', 'Can delete custom users'),
        ]

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_permissions',
        related_query_name='customuser_permission',
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='customuser_groups',
        related_query_name='customuser_group',
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
    )

    # def create_user_from_social(self, username, email, **extra_fields):
    #     extra_fields.setdefault('is_verified', True)
    #     return self.create_user(username, '', email, **extra_fields)


# # from allauth.account.adapter import DefaultAccountAdapter
# from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
# from .models import CustomUser

# class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
#     def save_user(self, request, sociallogin, form=None):
#         user = super().save_user(request, sociallogin, form)
#         user.is_verified = True  # Set is_verified to True for social media signups
#         user.save()
#         return user



   

class Storedotps(models.Model):
    email_id=models.EmailField()
    otp=models.CharField(max_length=6)
    otp_active=models.BooleanField(default=True)
    valid_from=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.email_id

from django.db import models
from django.utils import timezone

class EmailVerificationToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Token for {self.user.email}'
    

class DeleteVerificationToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Token for {self.user.email}'