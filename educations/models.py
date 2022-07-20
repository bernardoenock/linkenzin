import black
from django.db import models

# def upload_image_certificate(instance, filename):
#     return f"{instance.id_education}-{filename}"

class Education(models.Model):
    institution_name = models.CharField(max_length=255)
    course = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    certificate = models.ImageField(
        upload_to="certificates_pics", blank=True, null=True
        )
    curriculum = models.FileField(upload_to="curriculuns_files", blank=True, null=True)

    account = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="account",
        default=None,
    )
    
    def __str__(self):
        return f'{self.course}-{self.institution_name}'

   
