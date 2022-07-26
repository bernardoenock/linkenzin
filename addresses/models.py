from django.db import models

class Address(models.Model):
    zip_code = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    number = models.IntegerField()
    complement = models.CharField(max_length=255, default="House")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    country = models.CharField(max_length=20)

    def __str__(self):
        if self.complement:
            return f"Zip: {self.zip_code}/Number: {self.number} - {self.complement}"

        return f"Zip: {self.zip_code}/Number: {self.number}"