"""plaid_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from oauth2_provider.views import TokenView, RevokeTokenView 
from Item.views import AccessTokenCreate, handleWebhook
from plaid_django.views import CreateUser

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    path('signup/', CreateUser.as_view(), name='Create_User'),
    path('login/', TokenView.as_view(), name='User_Login'),
    path('logout/', RevokeTokenView.as_view(), name='User_Logout'),

    path('public_key/', AccessTokenCreate.as_view(), name='Create_AccessToken'),
    
    path('wh/', handleWebhook, name='Handel_webhook'),

]
