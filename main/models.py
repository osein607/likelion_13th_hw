from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
  name=models.CharField(max_length=30, null=False, blank=False)

  def __str__(self):
    return self.name
  
class Post(models.Model):
  title = models.CharField(max_length=50)
  writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE) #User:Post 1:N
  content = models.TextField()
  pub_date = models.DateTimeField()
  mbti = models.CharField(max_length=50)
  image = models.ImageField(upload_to="post/", blank=True, null=True)
  tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

  def __str__(self):
    return self.title

  def summary(self):
    return self.content[:20]

class Comment(models.Model):
  content = models.TextField()
  pub_date = models.DateTimeField()
  writer = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
  post = models.ForeignKey(Post, null=True, blank=False, on_delete=models.SET_NULL)

  def __str__(self):
    return self.post.title + ":" + self.content[:20] + "by" + self.writer.profile.nickname