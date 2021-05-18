from django.db import models

class Blog(models.Model):
   title = models.CharField(max_length=20)
   blog_description = models.TextField()
   date_posted = models.DateField()

   def __str__(self):
      return self.title