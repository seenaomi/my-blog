from django.db import models
from django.utils import timezone
from colorful.fields import RGBColorField



class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def approved_comment(self):
		return self.comment.filter(approved_comment=True)	


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comment')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Tag(models.Model):
    color = RGBColorField()
        


