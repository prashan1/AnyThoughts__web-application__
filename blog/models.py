from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	HashTag = models.CharField(max_length=100,blank=True,null=True)
	time_added = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.author}'

	def get_absolute_url(self,**kwargs):
		return reverse('detail-post',kwargs={'pk':self.pk})