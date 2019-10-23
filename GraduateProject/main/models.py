from django.db import models
from django.contrib import admin
from .system.storage import ImageStorage
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
# 	name = models.CharField(max_length=50)
# 	account = models.CharField(max_length=50)
# 	password = models.CharField(max_length=50)

# 	def __str__(self):
# 		return self.name

class Img(models.Model):

	# img_id = models.CharField(max_length=50)
	img_url = models.ImageField(upload_to='img', storage=ImageStorage())
	computerScore =  models.FloatField(null = True, blank = True)
	like = models.IntegerField(null = True, blank = True)
	create_time = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)

	# def __str__(self):
		# return self.img_id

class Comment(models.Model):

	comment_id = models.CharField(null = True, blank = True, max_length=50)
	content = models.TextField(null = True, blank = True)
	create_time = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	img = models.ForeignKey('Img', on_delete=models.CASCADE, null = True, blank = True)

	'''def __str__(self):
		return self.commend_id'''


