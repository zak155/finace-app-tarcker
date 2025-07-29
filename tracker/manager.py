from django.db import models
class TransactionQuerySet(models.QuerySet):
     def get_expense(self):
          return self.filter(type='expense')
     def get_income(self):
          return self.filter(type="income")
     def get_expense_total(self):
          return self.get_expense().aggregate(
               total=models.Sum('amount')
                 )['total'] or 0
     def get_income_total(self):
          return self.get_income().aggregate(
               total=models.Sum('amount')
                 )['total'] or 0      