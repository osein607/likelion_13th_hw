from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
  path('', mainpage, name="mainpage"),
  path('second', secondpage, name="secondpage"),
  path('new-post', new_post, name="new-post"),
  path('create', create, name="create"),
  path('<int:id>', detail, name="detail"),
  path('edit/<int:id>', edit, name="edit"),
  path('update/<int:id>', update, name="update"),
  path('delete/<int:id>', delete, name="delete"),
  path('comment_delete/<int:id>', comment_delete, name="comment_delete"),
  path('tag-list', tag_list, name="tag-list"),
  path('tag-posts/<int:tag_id>', tag_posts, name="tag-posts"),
  path('likes/<int:post_id>', likes, name="likes")
  
]








