from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    # A required line - links a UserProfile to User.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images',
                                default='/home/x/code/movie_rating_project/media/profile_images/sample_profile.jpg')

    def __unicode__(self):
        return self.user.username


class User(models.Model):
    name = models.EmailField(max_length=128, primary_key=True)
    password = models.CharField(max_length=20)
    dob = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __unicode__(self):
        return self.name


#------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------


class Movie(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    releaseYear = models.DateTimeField(auto_now=True, auto_now_add=True)
    coverPhoto = models.ImageField(upload_to='movie_images', default='media/profile_images/rango.jpg')
    trailer = models.URLField(blank=True)
    description = models.TextField(max_length=1000)


    def __unicode__(self):
        return self.name


class MoviePage(models.Model):
    movie = models.ForeignKey(Category)


    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    releaseYear = models.DateTimeField(auto_now=True, auto_now_add=True)
    coverPhoto = models.ImageField(upload_to='movie_images', default='media/profile_images/rango.jpg')
    trailer = models.URLField(blank=True)
    description = models.CharField(max_length=500)


    def __unicode__(self):
        return self.name


class Ratings(models.Model):
    name = models.ForeignKey(User)
    movieName = models.ForeignKey(Movie)
    rates = models.IntegerField(max_length=5)


class Comments(models.Model):
    name = models.ForeignKey(User)
    MovieName = models.ForeignKey(Movie)
    comment = models.CharField(max_length=500, null=False)
    commentDate = models.DateField()