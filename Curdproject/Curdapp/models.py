from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='movie_images')
    description = models.CharField(max_length=200)
    released_at = models.DateField(auto_now=True)


    def _str_(self):
        return self.name


class Slides(models.Model):
    name = models.CharField(max_length=255)
    image= models.ImageField(upload_to="images")

    def _str_(self):
        return self.name
