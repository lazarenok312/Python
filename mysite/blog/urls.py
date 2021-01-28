from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('posts/create_comment', views.create_comment, name='create_comment'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
