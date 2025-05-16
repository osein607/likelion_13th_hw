from django.shortcuts import render, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from main.models import Post

def mypage(request, id):
  user=get_object_or_404(User, pk=id)
  posts = Post.objects.filter(writer=user)

  context = {
    'user':user,
    'posts':posts,
  }
  return render(request, 'users/mypage.html', context)


