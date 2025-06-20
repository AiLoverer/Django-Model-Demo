"""
URL configuration for modelproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from modelapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('users/', views.person_list, name='person_list'),
    path('users/add/', views.person_add, name='person_add'),
    path('users/insert/', views.person_insert, name='person_insert'),
    path('users/delete/<int:pk>/', views.person_delete, name='person_delete'),
    path('users/edit/<int:pk>/', views.person_edit, name='person_edit'),
    path('users/update/', views.person_update, name='person_update'),
]
