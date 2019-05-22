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
from django.views.generic import RedirectView
from django.urls import path, include
from oauth2_provider.views import TokenView, RevokeTokenView 
from Item.views import AccessTokenCreate, handleWebhook, TransactionList, fireWebhook
from plaid_django.views import CreateUser, Login, Logout

urlpatterns = [
    path('',  RedirectView.as_view(url='/static/')),
    path('admin/', admin.site.urls),
    
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    path('signup/', CreateUser.as_view(), name='Create_User'),
    path('login/', Login, name='User_Login'),
    path('logout/', Logout, name='User_Logout'),

    path('public_token/', AccessTokenCreate.as_view(), name='Create_AccessToken'),
    path('transactions/', TransactionList.as_view(), name='Transaction_list'),
    
    path('wh/', handleWebhook, name='Handel_webhook'),
    path('firewh/', fireWebhook, name='Fire_webhook'),

]
