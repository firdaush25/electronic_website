# from django.db import models

# # Create your models here.


from django.db import models
from django.db import models

class Contact(models.Model):
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return str(self.date)









# from django.contrib.auth.models import User
# from app.models import register




# class Register(models.Model):
#     name = models.CharField(max_length=122)
#     username=models.CharField(max_length=122)
#     email = models.CharField(max_length=122)
#     phone = models.CharField(max_length=122)
#     password = models.CharField(max_length=122)
#     Cpassword = models.CharField(max_length=122)

# def __str__(self):
#     return self.name
