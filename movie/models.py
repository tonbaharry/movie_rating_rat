from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=200, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0 )
    #sale_end_time = models.DateField(help_text="date field needs formatting")
    #releaseYear = models.DateTimeField(auto_now=True, auto_now_add=True)
    #coverPhoto = models.ImageField(upload_to='movie_images', default='media/profile_images/rango.jpg')
    #trailer = models.Field(blank=True)
    description = models.TextField(help_text="Please add a movie description")


    def __unicode__(self):
        return self.name


class Comment(models.Model):
    movie = models.ForeignKey(Movie)
    views = models.IntegerField(default=0)
    description = models.TextField(max_length=500)

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


