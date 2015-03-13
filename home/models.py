from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dictionary(models.Model):
    description = models.CharField(max_length=1500)
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name, self.description
    
class Menue(models.Model):
  title = models.CharField(max_length=50)
  subtitle = models.CharField(max_length=1000)

  def getSubtitle(self):
    return [SubMenue(sub) for sub in self.subtitle.split(',')]

  def renderLink(self):
    return "_".join(self.title.lower().strip().split(" "))

class SubMenue:
  def __init__(self, name):
    self.name = name
  def renderLink(self):
    return "_".join(self.name.lower().strip().split(" "))

class Post(models.Model):
  name = models.CharField(max_length=100)
  content = models.CharField(max_length=6000)
  singular = models.BooleanField()

class Schema(models.Model):
  version = models.IntegerField()

class TextPost(models.Model):
  name = models.CharField(max_length=100, unique='true')
  value = models.CharField(max_length=100)
  
class User_Post_Link(models.Model):
  post = models.ForeignKey('TextPost')
  user = models.ForeignKey(User)

class User_Slide_Link(models.Model):
  user = models.ForeignKey(User)
  page = models.CharField(max_length=100)
  slides = models.IntegerField(default=0)

