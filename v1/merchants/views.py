from rest_framework.response import Response
from rest_framework.views import APIView
from v1.merchants.serializers import MerchantSerializer


class MerchantSignup(APIView):
    def post(self, request):
        merchant_serializer = MerchantSerializer(data=request.data)

        if merchant_serializer.is_valid(raise_exception=True):
            merchant_serializer.save()

            print('merchant signup success')

            return Response(data='merchant signup success')



