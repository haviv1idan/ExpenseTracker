from rest_framework import serializers
from .models import Transaction, OverseasTransactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class OverseasTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverseasTransactions
        fields = '__all__'
