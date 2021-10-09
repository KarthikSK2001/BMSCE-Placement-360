from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class CategoryInt(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class Post(models.Model):
	student_Name = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	Company_Logo = models.ImageField(null=True, blank=True, upload_to="images/")
	hiring_type = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	Interview_Rounds_with_detailed_description = RichTextField(blank=True, null=True)
	#body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	year_of_hiring = models.CharField(max_length=255, default='2019')
	number_hired_with_role = models.CharField(max_length=255)
	compensation_Details = models.CharField(max_length=255)
	Additional_Topics = RichTextField(blank=True, null=True)
	likes = models.ManyToManyField(User, related_name='blog_posts')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.company + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

class Postint(models.Model):
	student_Name = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	Company_Logo = models.ImageField(null=True, blank=True, upload_to="images/")
	hiring_type = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	Interview_Rounds_with_detailed_description = RichTextField(blank=True, null=True)
	#body = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	year_of_hiring = models.CharField(max_length=255, default='2019')
	number_hired_with_role = models.CharField(max_length=255)
	compensation_Details = models.CharField(max_length=255)
	Additional_Topics = RichTextField(blank=True, null=True)
	likes_int = models.ManyToManyField(User, related_name='blog_posts_int')

	def total_likes_int(self):
		return self.likes_int.count()

	def __str__(self):
		return self.company + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('article-detail', args=(str(self.id)) )
		return reverse('home')

 
class Profile(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	bio = models.TextField()
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
	website_url = models.CharField(max_length=255, null=True, blank=True)
	linkedin_url = models.CharField(max_length=255, null=True, blank=True)
	email = models.CharField(max_length=255, null=True, blank=True)



	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('home')



class Comment(models.Model):
	post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s ' % (self.post.company)

class Commentint(models.Model):
	postint = models.ForeignKey(Postint, related_name="commentsint", on_delete=models.CASCADE)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s ' % (self.postint.company)
		