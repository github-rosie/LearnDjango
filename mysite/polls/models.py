
"""
https://docs.djangoproject.com/en/5.0/intro/tutorial02/
https://docs.djangoproject.com/en/5.0/topics/db/queries/
https://docs.djangoproject.com/en/5.0/ref/models/relations/
https://docs.djangoproject.com/en/5.0/topics/db/queries/#field-lookups-intro


The migrate command takes all the migrations that have not been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. 

The three-step guide to making model changes:
- Change your models (in models.py).
- Run python manage.py makemigrations polls to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.
"""

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# Question is a subclass of models.Model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        """It is important to add __str__() methods to models, not only for your own convenience when dealing with the interactive prompt, but also because objects representations are used throughout Djangos automatically-generated admin.
        """
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        minus_one_day = now - datetime.timedelta(days=1)
        return minus_one_day <= self.pub_date <= now


# Choice is a subclass of models.Model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text