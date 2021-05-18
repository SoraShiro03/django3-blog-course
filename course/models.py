from django.db import models
from django_resized import ResizedImageField
#from PIL import Image



class Course(models.Model):
   title = models.CharField(max_length=30)
   description = models.TextField()
   date_posted = models.DateField()
   image = models.ImageField(upload_to= "course/images/")


