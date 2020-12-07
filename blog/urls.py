from django.urls import path
from . import views

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('test',views.test,name='test'),
    path('post_detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit',views.post_edit,name='post_edit'),
    path('post/<int:pk>/remove',views.post_remove,name='post_remove'),
    # path('about_list',views.about_list,name='about_list'),
]