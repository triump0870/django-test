from django.db import models

# Create your models here.
class Article(models.Model):
	"""This is the Article class. It contains title, body, publication date and likes"""
	title = models.CharField(max_length = 200)
	body = models.TextField()
	pub_date = models.DateTimeField('date published')
	likes = models.IntegerField()
		