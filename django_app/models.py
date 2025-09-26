from django.db import models

# Create your models here.


class Demo(models.Model):
    """
    Demo model with name and description fields for the DB Demo page.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
