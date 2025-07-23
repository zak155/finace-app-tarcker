import django_filters
from tracker.models import Transaction

class TransactionFilter(django_filters.FilterSetilterset):
      transaction_type=django_filters.ChoiceFilter(
            choices=Transaction.TRANSACTION_TYPE_CHOICES,
            field_name='type',
            lookup_expr='iexact',
            empty_level='Any'
      )

      class Meta:
            model=Transaction
            fileds=('transaction_type')