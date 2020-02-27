from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Job object: {self.title} {self.location} I.D.:{self.id}"
