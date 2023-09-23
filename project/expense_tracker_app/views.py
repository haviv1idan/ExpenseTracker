from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Transaction, OverseasTransactions
from .serializers import TransactionSerializer, OverseasTransactionSerializer

# Create your views here.


# Transactions
class TransactionListView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionCreateView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionUpdateView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDeleteView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ClearTransactionTableView(APIView):
    def post(self, request, format=None):
        try:
            # Clear all rows from the Transaction table
            Transaction.objects.all().delete()
            return Response({'message': 'Table cleared successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Overseas transactions
class OverseasTransactionListView(generics.ListAPIView):
    queryset = OverseasTransactions.objects.all()
    serializer_class = OverseasTransactionSerializer

class OverseasTransactionCreateView(generics.CreateAPIView):
    queryset = OverseasTransactions.objects.all()
    serializer_class = OverseasTransactionSerializer

class OverseasTransactionUpdateView(generics.UpdateAPIView):
    queryset = OverseasTransactions.objects.all()
    serializer_class = OverseasTransactionSerializer

class OverseasTransactionDeleteView(generics.DestroyAPIView):
    queryset = OverseasTransactions.objects.all()
    serializer_class = OverseasTransactionSerializer
