from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from v1.merchants.models import Merchant
from v1.stores.serializers import StoreSerializer


class StoreRegister(APIView):
    def post(self, request):
        store_serializer = StoreSerializer(data=request.data)

        if store_serializer.is_valid(raise_exception=True):
            store_serializer.save()

            print('store register success')

            return Response(data='store register success')



