from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('addpost/',views.addpost,name='addpost'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('userposts/',views.userposts,name='userposts'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('detail_view/<int:pk>',views.Detail_View.as_view(),name='detail_view'),
]
