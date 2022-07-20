from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import CustomUserManager


class GenderFieldChoice(models.TextChoices):
    cisgender = ("Cisgender",)
    transgender = ("Transgender",)
    non_binary = ("Non Binary",)

class TypeAccountChoice(models.TextChoices):
    boss = ("Boss",)
    recruiter = ("Recruiter",)
    candidate = ("Candidate",)
    hired = ("Hired",)
    admin = ("Admin",)


class Account(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    gender = models.CharField(
        max_length=50,
        choices=GenderFieldChoice.choices
    )
    type_account = models.CharField(
        max_length=50,
        choices=TypeAccountChoice.choices,
        default=TypeAccountChoice.admin
    )
    
    is_staff_company = models.BooleanField(default=False)


    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    address = models.OneToOneField("addresses.Address", on_delete=models.CASCADE, null=True)

    # company = models.ForeignKey(
    # "companies.Company", on_delete=models.CASCADE, related_name="accounts", null=True
    # )

    username = None
    is_staff = None
    date_joined = None
    
    USERNAME_FIELD = "email"
    IS_STAFF_FIELD = "is_staff_company"
    DATE_JOINED_FIELD = "create_at"
    
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "cpf",
        "gender",
        "phone",
    ]
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.type_account}"


    
