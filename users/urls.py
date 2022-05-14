from django.urls import path, include

from .views import SignupView, UpdateUserView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('sign-up/', SignupView.as_view(), name='sign-up'),
    path('update-user/<int:pk>', UpdateUserView.as_view(), name='update-user'),
]