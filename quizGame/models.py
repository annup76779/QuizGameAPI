from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class SubjectArea(models.Model):
    name = models.CharField(max_length=225, unique=True)  # cannot be null, it is Varchar(225)


class Test(models.Model):
    class TestStatusChoices(models.TextChoices):
        # Works as enum but works well with django OrM and only can be used with django orm
        Draft = '1', 'Draft'
        Published = "2", 'Published'
        Closed = "3", 'Closed'

    subjectID = models.ForeignKey(SubjectArea, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    dateCreated = models.DateTimeField(auto_now=True)  # first created date and time
    # updated_on = models.DateTimeField(auto_now_add=True)    #last updated date and time
    status = models.IntegerField(choices=TestStatusChoices.choices)


class Questions(models.Model):
    testID = models.ForeignKey(Test, on_delete=models.CASCADE)
    questionText = models.TextField()
    score = models.IntegerField()
    correctAnswer = models.TextField()


class Answers(models.Model):
    questionID = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answerText = models.TextField()
