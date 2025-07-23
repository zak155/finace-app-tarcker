from django.shortcuts import render
from tracker.models import Transaction
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'tracker/index.html')
@login_required
def transactions_list(request):
    transactions=Transaction.objects.filter(user=request.user).order_by('-date')
    context={'transactions':transactions}
    return render(request,'tracker/transactions-list.html',context)
    