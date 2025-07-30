from django.shortcuts import render
from tracker.models import Transaction
from django.contrib.auth.decorators import login_required
from tracker.filter import TransactionFilter
from tracker.forms import TransactionForm
from django_htmx.http import retarget
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

def createTransaction(request):
    if request.method =="POST":
        form=TransactionForm(request.POST)
        if form.is_valid():
           transaction=form.save(commit=False)
           transaction.user=request.user
           transaction.save()
           context={'message':"transaction created sucessfuly"}
           return render(request,'tracker/partials/transaction-success.html',context)
        else:
            context={'form':form}
            response=render(request,'tracker/partials/create_transaction.html',context)
            return retarget(response,"#transaction-block") 
    context={'form':TransactionForm()}
    return render(request,'tracker/partials/create_transaction.html',context)