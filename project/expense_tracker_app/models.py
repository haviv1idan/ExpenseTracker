from django.db import models

# Create your models here.
class Transaction(models.Model):
    date = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    credit_4_last_digits = models.IntegerField()
    expense_type = models.CharField(max_length=100)
    transaction_amount = models.FloatField()
    debit_currency = models.CharField(max_length=100)
    original_transaction_amount = models.FloatField()
    original_transaction_currency = models.CharField(max_length=100)
    billing_date = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'Date: {self.date}\n, Business Name: {self.business_name}\n, ' \
               f'Category: {self.category}\n, Credit 4 Last Digits: {self.credit_4_last_digits}\n, ' \
               f'Expense Type: {self.expense_type}\n, Transaction Amount: {self.transaction_amount}\n, ' \
               f'Debit Currency: {self.debit_currency}\n, Original Transaction Amount: {self.original_transaction_amount}\n, ' \
               f'Original Transaction Currency: {self.original_transaction_currency}\n, ' \
               f'Billing Date: {self.billing_date}\n, Payment Type: {self.payment_type}'
    

class OverseasTransactions(models.Model):
    date = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    credit_4_last_digits = models.IntegerField()
    expense_type = models.CharField(max_length=100)
    transaction_amount = models.FloatField()
    debit_currency = models.CharField(max_length=100)
    original_transaction_amount = models.FloatField()
    original_transaction_currency = models.CharField(max_length=100)
    billing_date = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    exchange_rate = models.CharField(max_length=100)

    def __str__(self):
        return f'Date: {self.date}\n, Business Name: {self.business_name}\n, ' \
               f'Category: {self.category}\n, Credit 4 Last Digits: {self.credit_4_last_digits}\n, ' \
               f'Expense Type: {self.expense_type}\n, Transaction Amount: {self.transaction_amount}\n, ' \
               f'Debit Currency: {self.debit_currency}\n, Original Transaction Amount: {self.original_transaction_amount}\n, ' \
               f'Original Transaction Currency: {self.original_transaction_currency}\n, ' \
               f'Billing Date: {self.billing_date}\n, Payment Type: {self.payment_type}\n,  exchange Rate: {self.exchange_rate}\n, '
    