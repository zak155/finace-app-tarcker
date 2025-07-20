import random
from faker import Faker
from django.core.management.base import BaseCommand
from tracker.models import User, Transaction, Category


class Command(BaseCommand):
    help = "Generates transactions for testing"

    def handle(self, *args, **options):
        fake=Faker()
        categories = [
            "Bills",
            "Food",
            "Clothes",
            "medical",
            "Housing",
            "Salary",
            "Social",
            "Transport",
            "Vacation",
        ]
        for category in categories:
            Category.objects.get_or_create(name=category)
        #get user        
        user=User.objects.filter(username='robel').first()  
        if not user:
             User.objects.create_superuser(username='sirak',password='test')      
             categories=Category.objects.all()
             types=[
              x[0] 
              for x in Transaction.TRANSACTION_TYPE_CHOICES
                ] 
             for i in range(20):
                 Transaction.objects.create(
                     category=random.choice(categories),
                     user=user,
                     amount=random.uniform(1,2500),
                     date=fake.date_between(start_date='-1yr',end_date='today'),
                     type=random.choice(types)
                 )
       