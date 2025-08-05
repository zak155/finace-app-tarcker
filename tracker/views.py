from django.shortcuts import render
from tracker.models import Transaction
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from tracker.filter import TransactionFilter
from tracker.forms import TransactionForm
from django_htmx.http import retarget
from django.shortcuts import get_object_or_404

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
def updateTransaction(request,pk):
    transaction=get_object_or_404(Transaction,pk=pk)
    if request.method == 'POST':
        form=TransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            transaction=form.save()
            context={'message':"Transaction was updated sucessfuly"}
            return render(request,'tracker/partials/transaction-success.html',context)
        else:
            context={'form':form,
                     'transaction':transaction
                     }
            response=render(request,'tracker/partials/update-transaction.html',context)
            return retarget(response,"#transaction-block") 
    context={
        'form':TransactionForm(instance=transaction),
        'transaction':transaction
    }

    return render(request,'tracker/partials/update-transaction.html',context)
@login_required
@require_http_methods(["DELETE"])
def deleteTransaction(request,pk):
    transaction=get_object_or_404(Transaction,pk=pk)
    transaction.delete()
    context={
        'message':f"Transaction of{transaction.amount} on {transaction.date} deleted sucessfully"
    }
    return render(request,'tracker/partials/transaction-success.html',context)
