from django.db import models

# Create your models here.

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations  

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    address = models.CharField(max_length=50,default="")
    message = models.TextField(max_length=200,default="")
    date = models.DateField() 

    def __str__(self):
        return self.name

# class Comments(models.Model):
#     sno = models.AutoField(primary_key = True)
#     comment = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = 
#     parent = 
