from django.db import models

# Create your models here.
class databse(models.Model):
    id =models.AutoField(primary_key=True)
    Email =models.EmailField( max_length=254)
    UserName =models.CharField(max_length=50)
    Address =models.CharField(max_length=100)
    Password =models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)
    