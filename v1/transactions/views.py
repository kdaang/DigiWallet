from django.core import serializers
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from v1.transactions.models import Transaction
from v1.transactions.serializers import TransactionSerializer


class GetTransaction(APIView):
    def get(self, request):
        transactions = Transaction.objects.get_transactions(user=request.user.pk)
        transactions_serializer = TransactionSerializer(transactions, many=True)

        return Response(data=transactions_serializer.data)


class PostMerchantTransaction(APIView):
    def post(self, request):
        data = request.data
        data['from_user'] = request.user.pk

        transaction_serializer = TransactionSerializer(data=data, context={'request': request})

        if transaction_serializer.is_valid(raise_exception=True):
            transaction_serializer.save()

            print('transaction success')

            return Response(data='transaction success')