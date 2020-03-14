from django.urls import path,include
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from rest_framework import routers
from users import views as user_views
from django.conf.urls import include
from django.contrib import admin

"""router = routers.DefaultRouter()
router.register('post',views.PostView)
"""
urlpatterns = [
    path('', PostListView.as_view(),name = 'movie-home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name = 'post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name = 'post-delete'),
    path('post/new/', PostCreateView.as_view(),name = 'post-create'),
    path('about/', views.about,name = 'movie-about')
]