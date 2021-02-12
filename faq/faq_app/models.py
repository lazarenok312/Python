import datetime
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
class UserQuestion(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.CharField(max_length=255)
	pub_date = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.title

class Answer(models.Model):
	question = models.ForeignKey(UserQuestion, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.CharField(max_length=255)
	pub_date = models.DateTimeField(default=timezone.now())
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	best_answer = models.BooleanField(default=False)

	class Meta:
		ordering = ['pub_date']
		verbose_name = "Ответ"
		verbose_name_plural = "Ответы"

	def __str__(self):
		return 'Ответ {} от {} к вопросу {}'.format(self.body, self.user.username, self.question.title)

class UserLikes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	like_date = models.DateTimeField(default=timezone.now())

class UserDislikes(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	dislike_date = models.DateTimeField(default=timezone.now())