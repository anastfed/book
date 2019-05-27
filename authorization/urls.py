from django.urls import re_path
import authorization.views as authorization

app_name = 'authorization'

urlpatterns = [
    re_path('login/$', authorization.user_login, name='login'),
    re_path('logout/$', authorization.user_logout, name='logout'),
    re_path('register/$', authorization.user_register, name='register'),
    re_path('edit/$', authorization.user_edit, name='edit'),
]