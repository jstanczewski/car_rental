import django.db.models as models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models import CharField, IntegerField, EmailField
from django.contrib.auth.models import Group, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(
        self,
        first_name,
        second_name,
        document_number,
        age,
        address,
        email_address,
        phone_number,
        password=None,
    ):
        if not email_address:
            raise ValueError("Users must have an email address")
        user = self.model(
            email_address=self.normalize_email(email_address),
            first_name=first_name,
            second_name=second_name,
            document_number=document_number,
            age=age,
            address=address,
            phone_number=phone_number,
        )
        group = Group.objects.all()
        user.groups.add(*group)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        first_name,
        second_name,
        document_number,
        age,
        address,
        email_address,
        phone_number,
        password=None,
    ):
        user = self.create_user(
            first_name=first_name,
            second_name=second_name,
            document_number=document_number,
            age=age,
            address=address,
            email_address=email_address,
            phone_number=phone_number,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    first_name = CharField(max_length=50)
    second_name = CharField(max_length=50)
    document_number = CharField(max_length=15)
    age = IntegerField()
    address = CharField(max_length=100)
    email_address = EmailField(unique=True)
    phone_number = CharField(max_length=15)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email_address"
    REQUIRED_FIELDS = [
        "first_name",
        "second_name",
        "document_number",
        "age",
        "address",
        "phone_number",
    ]

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
