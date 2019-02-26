"""apiPaintBall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from user.models import User
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from user.api.viewset import UserListViewSet
from user.api.viewset import UserRegistrationAPIView
from django.contrib.auth import views as auth_views
from game.api.viewset import GameList, GameDetails
from game.models import Game
from advertisement.api.viewset import AdvertisementListViewSet
from advertisement.models import Advertisement

from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'user', UserListViewSet, base_name='User')
router.register(r'register', UserRegistrationAPIView, base_name=User)
router.register(r'games', GameList, base_name=Game)
router.register(r'ad', AdvertisementListViewSet, base_name=Advertisement)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('register/', UserRegistrationAPIView.as_view()),
    # path('register/', UserRegistrationAPIView.as_view()),
    #path('api/registration/', include('django_rest_passwordreset.urls', namespace='registration')),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='registration'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api-token-auth/', obtain_auth_token),
]
