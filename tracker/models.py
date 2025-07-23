from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
class Category(models.Model):
     name=models.CharField(max_length=30,unique=True)
     class Meta:
          verbose_name_plural='Categories'#which hepls us to protect
          #the admin panel to not add s after table name(Category) 
     def __str__(self):
         return self.name      
class Transaction(models.Model):
      TRANSACTION_TYPE_CHOICES=(
           ('income','INCOME'),
           ('expense','EXPENSE')
      )
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      category=models.ForeignKey(Category,on_delete=models.CASCADE)
      type=models.CharField(max_length=20,choices=TRANSACTION_TYPE_CHOICES)
      amount=models.DecimalField(max_digits=10,decimal_places=2)
      date=models.DateField()
      
      def __str__(self):
           return f"{self.type} of {self.amount} on {self.date} by {self.user}"
      class Meta:
           ordering=['-date']