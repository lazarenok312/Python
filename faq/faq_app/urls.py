from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'faq'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('question/<int:pk>/', views.UpdateQuestionView.as_view(), name='update_question'),
	path('question/delete/<int:pk>/', views.DeleteQuestionView.as_view(), name='delete_question'),
	path('question/new', views.CreateQuestionView.as_view(), name='new_question'),
	path('users/register', views.RegisterView.as_view(), name='register')
]