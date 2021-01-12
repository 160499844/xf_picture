"""xf_picture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('group/', getImages),
    path('update/', update),
    path('api/getPage/', getImgPage),
    path('api/m/getPage/', getVideoPage),
    path('home/', getMyFolderItem),
    path('details/', details),
    path('play/', play),
    path('movies/', movies),
    path('login_view/', login_view),
    path('logout_system/', logout_system),
    path('', to_login_view),
]
