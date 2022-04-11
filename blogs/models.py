from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
	reporter=models.ForeignKey(User, on_delete=models.CASCADE , blank=True , null=True)
	pub_date=models.DateTimeField()
	headline=models.CharField(max_length=200)
	slug=models.CharField(max_length=200)
	content=models.TextField()
	institution_name=models.CharField(max_length=100)
	institution_website=models.CharField(max_length=100)
	institution_acronmy=models.CharField(max_length=20)
	post_image=models.ImageField(null=True, blank=True,upload_to='Post-img/')


	@property
	def image_url(self):
		if self.post_image and hasattr(self.post_image,'url'):
			return self.post_image.url
		return None

	def __str__ (self):
		return self.headline



  
class Comment(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	body=models.TextField()
	detil=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
	comment_image=models.ImageField(null=True, blank=True, upload_to='comment-img/')

	@property
	def image_url(self):
		if self.comment_image and hasattr(self.comment_image,'url'):
			return self.comment_image.url
		return None
	
	
	def __str__(self):
		return self.body

class CommentReply(models.Model):
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

class Carousel (models.Model):
	image=models.ImageField(upload_to="img")
	title=models.CharField(max_length=100)
	body=models.TextField()
	def __str__(self):
		return self.title