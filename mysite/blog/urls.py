from django.urls import path, include


from blog import views


urlpatterns = [
    path(r'about/', views.AboutView.as_view(), name='about'),
    path(r'', views.PostListView.as_view(), name='post_list'),
    path(r'post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path(r'post/new/', views.PostCreateView.as_view(), name='post_new'),
    path(r'post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path(r'post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path(r'drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path(r'post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path(r'post/<int:pk>/publish', views.post_publish, name='post_publish'),
    path(r'comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path(r'comment/<int:pk>/delete/', views.remove_comment, name='remove_comment'),
]
