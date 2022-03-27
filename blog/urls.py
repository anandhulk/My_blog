from django.urls import path
from blog import views

urlpatterns=[
    path('',views.index),
    path('posts',views.posts),
    path('posts/<slug:slug>',views.detail)
]