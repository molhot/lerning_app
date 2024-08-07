from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_lenght = 200)
    pub_data = models.DateField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_lenght = 200)
    votes = models.IntegerField(default = 0)
