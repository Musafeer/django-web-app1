from django.urls import re_path
from helloworld import views

app_name = 'helloworld'

urlpatterns=[
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
    re_path(r'^dashboard/$',views.dashboard,name='dashboard'),
]