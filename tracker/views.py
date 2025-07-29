from django.shortcuts import render
from tracker.models import Transaction
from django.contrib.auth.decorators import login_required
from tracker.filter import TransactionFilter

# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')
@login_required
def transactions_list(request):
    transactions_filter=TransactionFilter(
        request.GET,
        queryset=Transaction.objects.filter(user=request.user)

    )
    total_income=transactions_filter.qs.get_income_total()
    total_expense=transactions_filter.qs.get_expense_total()
    context={
        'filter':transactions_filter,
        'total_income':total_income,
        'total_expense':total_expense,
        'net_income':total_income-total_expense,
        }
    if request.htmx:
       return render(request,'tracker/partials/transaction-container.html',context) 
    return render(request,'tracker/transactions-list.html',context)
    