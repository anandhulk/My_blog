from django.urls import path
from blog import views

urlpatterns=[
    path('',views.index,name="index"),
    path('posts',views.posts,name="allposts"),
    path('posts/<slug:slug>', views.detail, name="details")
]