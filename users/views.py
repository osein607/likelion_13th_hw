from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import Post

def mypage(request, id):
  print("📌 접속한 유저 ID:", id, type(id))
  user=get_object_or_404(User, pk=id)
  posts = Post.objects.filter(writer=user.username)

  # #print("📌 해당 유저:", user.username)
  # #print("📌 해당 이름:", post.writer)
  # print("📌 글 개수:", posts.count())

  context = {
    'user':user,
    'posts':posts,
  }
  return render(request, 'users/mypage.html', context)


