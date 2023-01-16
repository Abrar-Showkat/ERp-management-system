from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register', views.register_user.as_view()),
    path('employees', views.employee_list.as_view()),
    path('employee/register', views.register_employee.as_view()),
    path('employee/<int:pk>/', views.employee_detail.as_view()),
    path('employee/forgot_password', views.forgot_password.as_view()),
    # we have to provide token in header for login with email and passowrd
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),

]
