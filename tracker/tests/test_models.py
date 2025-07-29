import pytest
from tracker.models import Transaction

@pytest.mark.djangodb
def test_queryset_get_income_method(transactions):
    qs=Transaction.objects.get_income()
    assert qs.count()>0
    assert all(
        [transaction.type=='income' for transaction in qs]
    )
@pytest.mark.djangodb
def test_queryset_get_expense_method(transactions):
    qs=Transaction.objects.get_expense()
    assert qs.count()>0
    assert all(
        [transaction.type=='expense' for transaction in qs]
    )  
@pytest.mark.djangodb
def test_queryset_get_income_total(transactions):
    total_expense=Transaction.objects.get_income_total()
    assert total_expense==sum(t.amount for t in transactions if t.type=='income')  
@pytest.mark.djangodb
def test_queryset_get_expense_total(transactions):
    total_expense=Transaction.objects.get_expense_total()
    assert total_expense == sum(t.amount for t in transactions if t.type=='expense')         