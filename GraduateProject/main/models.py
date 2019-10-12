from django.db import models

from django.contrib import admin

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=50)
	account = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Img(models.Model):

	# img_id = models.CharField(max_length=50)
	img_url = models.ImageField(upload_to='img')
	computerScore =  models.IntegerField()
	like = models.IntegerField()
	create_time = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey('User', on_delete=models.CASCADE)

	# def __str__(self):
		# return self.img_id

class Commend(models.Model):

	commend_id = models.CharField(max_length=50)
	content = models.TextField()
	create_time = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey('User', on_delete=models.CASCADE)
	img = models.ForeignKey('Img', on_delete=models.CASCADE)

	def __str__(self):
		return self.commend_id


admin.site.register(User)
admin.site.register(Img)
admin.site.register(Commend)