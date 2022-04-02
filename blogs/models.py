from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
	reporter=models.ForeignKey(User, on_delete=models.CASCADE , blank=True , null=True)
	pub_date=models.DateTimeField()
	headline=models.CharField(max_length=200)
	slug=models.CharField(max_length=200)
	content=models.TextField()

	def __str__ (self):
		return self.headline

  
class Comment(models.Model):
	# commenter=models.CharField(max_length=50)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	body=models.TextField()
	detil=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
	
	
	def __str__(self):
		return self.body

class CommentReply(models.Model):
	# commenter=models.CharField(max_length=50)
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	body=models.TextField()
	detil=models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='reply')
	
	def __str__(self):
		return self.body

# Edublog help section
class RoommateHelp (models.Model):
	user=models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	message=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.message
