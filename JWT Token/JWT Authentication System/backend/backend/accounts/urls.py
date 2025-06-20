from django.urls import path
from .views import * 
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegestrationAPIView.as_view(), name='register-user'),
    path('login/', UserLoginAPIView.as_view(), name='login-user'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout-user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserDetailAPIView.as_view(), name='user-detail'),
]
