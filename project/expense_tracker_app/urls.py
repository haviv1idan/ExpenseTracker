from django.urls import path
from . import views

# expense_tracker_app/urls.py

from django.urls import path
from .views import TransactionListView,TransactionCreateView, TransactionUpdateView, TransactionDeleteView

urlpatterns = [
    path('transactions/all/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/create/', TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction-update'),
    path('transactions/delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('transactions/clear-transaction-table/', views.ClearTransactionTableView.as_view(), name='clear_transaction_table'),
]

