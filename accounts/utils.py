from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_superuser, is_staff_company, **extra_fields
    ):
  

        if not email:
            print(email)
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_superuser=is_superuser,
            is_staff_company=is_staff_company,
            is_active=True,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, is_staff_company=False, **extra_fields):
        return self._create_user(
            email, password, False, is_staff_company, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, False, **extra_fields)
