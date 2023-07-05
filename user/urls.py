from django.urls import path
from .views import CreateUserView, TokenObtainView

urlpatterns = [
    path('user/token/', TokenObtainView.as_view(), name='obtain-token'),
    path('user/create/', CreateUserView.as_view(), name='crear-usuario'),
]
