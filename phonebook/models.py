from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    user = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            null=True,
    )
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('id', )


