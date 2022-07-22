from django.db import models

class Skill(models.Model):

    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __repr__(self) -> str:
        return f"Skill - {self.title}"