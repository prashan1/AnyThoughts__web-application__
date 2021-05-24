from django.urls import path
from . import views

urlpatterns = [
	path('', views.PostHomeView.as_view(), name='blog-home' ),
	path('user/<str:username>/', views.UserPostView.as_view(), name='user-post' ),
	path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail-post' ),
	path('create_post/', views.CreatePostView.as_view(), name='create-post' ),
	path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete-post' ),
	path('post/<int:pk>/update_post/', views.UpdatePostView.as_view(), name='update-post' ),
]