from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView


urlpatterns=[

    path('', PostListView.as_view(), name='ji'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('sagol/', views.sagol, name='jina'),
  




 ]
