from django.urls import path

from blogs.views import *

urlpatterns = [
    path('home/', home, name='home_page'),
    path('', register, name='register_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('addblog/', add_blog, name='blog_page'),
    path('bloglist/', blog_list, name='blog_list_page'),
    path('edit/<str:b_id>/', blog_edit, name='blog_edit'),
    path('delete/<str:b_id>/', delete, name='delete'),
]