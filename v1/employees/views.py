from rest_framework.response import Response
from rest_framework.views import APIView
from v1.employees.serializers import EmployeeSerializer


class EmployeeSignup(APIView):
    def post(self, request):
        employee_serializer = EmployeeSerializer(data=request.data)

        if employee_serializer.is_valid(raise_exception=True):
            employee_serializer.save()

            print('employee signup success')

            return Response(data='employee signup success')
