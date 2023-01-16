from django.shortcuts import render
from .models import User, Employee
from rest_framework.views import APIView
from django.http import Http404, JsonResponse
from .serializers import UserSerializer, EmployeeSerializer
from rest_framework import status
import pyotp


# Permissions will be implemented on the end of project


class register_user(APIView):

    def post(self, request):

        if request.data['password'] == request.data['password2']:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data={'message': 'User created sucessfully'}, safe=False, status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(data={'message': "Passwords didn't match"}, status=status.HTTP_400_BAD_REQUEST)


class register_employee(APIView):

    def post(self, request):
        if request.data['password'] == request.data['password2']:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data={'message': 'Employee created successfull'}, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse(data={'message': "Password didn't match"}, status=status.HTTP_400_BAD_REQUEST)


class employee_list(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)


class employee_detail(APIView):

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)

        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST
                            )

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return JsonResponse(data={"message": "Employee is deleted"}, status=status.HTTP_204_NO_CONTENT)


class forgot_password(APIView):

    email = ""
    otp = ""

    def post(self, request):
        try:
            email = request.data['email']
            forgot_password.email = request.data['email']
            try:
                employee = Employee.objects.get(
                    email=email)
                employee.otp_counter += 1
                employee.save()
                secret_key = pyotp.random_base32()
                otp = pyotp.HOTP(secret_key)
                forgot_password.otp = otp.at(user.otp_counter)
                print(forgot_password.otp)  # for getting the otp

 # send otp               #send_mail('OTP for reset password',f'your otp is {otp.at(user.otp_counter)}', settings.EMAIL_HOST_USER, [email], fail_silently=False)

                return Response(message={'message': 'otp has been sent to your email'}, status=status.HTTP_200_OK)

            except ObjectDoesNotExist:
                return JsonResponse(data={"message": "This email is not found in our data"}, status=status.HTTP_404_NOT_FOUND)

        except:
            return JsonResponse(data={"message": "Either request data or request method is not correct"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        try:

            if forgot_password.otp == request.data['otp']:

                password = request.data['password']
                password2 = request.data['password2']

                if password == password2:

                    employee = Employee.objects.get(
                        email=forgot_password.email)

                    employee.set_password(password)
                    employee.save()

                    return JsonResponse(data={"message": "password Changed Succesfully"}, status=status.HTTP_200_OK)
                else:

                    return JsonResponse(data={"message": "Passwords didn't match. Try again!"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse(data={"message": "Otp is not correct"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return JsonResponse(data={"message": "Either data or method is not correct"}, status=status.HTTP_400_BAD_REQUEST)
