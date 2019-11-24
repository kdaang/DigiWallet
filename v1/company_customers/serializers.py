from rest_framework import serializers
from v1.company_customers.models import CompanyCustomer


class CompanyCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyCustomer
        fields = ['company', 'customer', 'points']

    def create(self, validated_data):
        return CompanyCustomer.objects.create_company_customer_data(**validated_data)

    def update(self, instance, validated_data):
        if instance.points + validated_data['points'] < 0:
            raise serializers.ValidationError(detail='balance can not be negative')

        instance.points += validated_data['points']
        instance.save()

        return instance
