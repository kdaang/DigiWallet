# Create your views here.
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from v1.merchants.models import Merchant
from v1.merchants.serializers import MerchantSerializer, UserSerializer


class MerchantView(APIView):
    def post(self, request):
        user = {'username':'username4', 'email': 'email2'}
        userSerializer = UserSerializer(data=user)
        print('VALID: ' + str(userSerializer.is_valid()))
        # data = {'user': user.id, 'name': request.data['name']}
        # merchant_serializer = MerchantSerializer(data=data)
        # if merchant_serializer.is_valid(raise_exception=True):
        #     user.save()
        #     merchant_serializer.save()
        return Response(data=request.data, status=status.HTTP_200_OK)
        # else:
        #     print(merchant_serializer.error_messages)

