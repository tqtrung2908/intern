from django.urls import path

from user.API.views import UserView, RegisterView, LoginView

urlpatterns = [
    path('user_list/', UserView.as_view(), name='api_user'),
    path('register/', RegisterView.as_view(), name='api_register'),
    path('login/', LoginView.as_view(), name='api_login'),
]