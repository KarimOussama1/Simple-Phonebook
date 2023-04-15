from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Phone(models.Model):
    number = models.CharField(max_length=20)
    contact = models.ForeignKey(
        Contact,
        related_name='phone_numbers',
        blank=True,
        null=True, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.number
