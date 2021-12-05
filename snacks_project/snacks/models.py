from django.db import models

# Create your models here.


class Things(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()

    def __str__(self):
        return self.title