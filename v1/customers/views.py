from rest_framework.response import Response
from rest_framework.views import APIView
from v1.customers.serializers import CustomerSerializer


class CustomerSignup(APIView):
    def post(self, request):
        customer_serializer = CustomerSerializer(data=request.data)

        if customer_serializer.is_valid(raise_exception=True):
            customer_serializer.save()

            print('customer signup success')

            return Response(data='customer signup success')
