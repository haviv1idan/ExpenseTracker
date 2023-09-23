from django.contrib import admin
from .models import Transaction, OverseasTransactions

class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'date', 
        'business_name', 
        'category', 
        'credit_4_last_digits', 
        'expense_type', 
        'transaction_amount',
        'debit_currency', 
        'original_transaction_amount', 
        'original_transaction_currency', 
        'billing_date', 
        'payment_type', 
    ) 
    list_filter =  list_display
    

class OverseasTransactionAdmin(admin.ModelAdmin):
    list_display = (
        'date', 
        'business_name', 
        'category', 
        'credit_4_last_digits', 
        'expense_type', 
        'transaction_amount',
        'debit_currency', 
        'original_transaction_amount', 
        'original_transaction_currency', 
        'billing_date', 
        'payment_type', 
        'exchange_rate'
    ) 
    list_filter = list_display
    

# Register your models here.
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(OverseasTransactions, OverseasTransactionAdmin)
