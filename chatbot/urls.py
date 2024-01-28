from django.urls import path
from . import views

urlpatterns=[
    path('chatbot',views.chatbot, name='chatbot'),
    path('',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout')


    
]





