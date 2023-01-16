from rest_framework import serializers
from .models import User, Employee
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:

        model = User
        fields = ['email', 'name', 'password', 'phone',
                  'country', 'business_name', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.country = validated_data.get('country', instance.country)
        instance.business_name = validated_data.get(
            'business_name', instance.business_name)
        instance.role = validated_data.get('role', instance.role)
        password = make_password(instance.password)
        instance.password = password
        instance.save()
        return instance


class EmployeeSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['name', 'email', 'password', 'phone', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        employee = Employee.objects.create(**validated_data)
        password = make_password(password)
        employee.password = password
        employee.save()
        return employee

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        password = make_password(instance.password)
        instance.password = password
        instance.phone = validated_data.get('phone', instance.phone)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance
