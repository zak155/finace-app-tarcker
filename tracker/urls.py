from django.urls import path
from tracker import views


urlpatterns = [
    path("", views.index, name='index'),
    path('transactions/',views.transactions_list,name='transactions-list'),
    path('transactions/create',views.createTransaction,name="create-transaction"),
    path('transactions/<int:pk>/update/',views.updateTransaction,name="update"),
    path('transactions/<int:pk>/delete/',views.deleteTransaction,name="delete")
]
