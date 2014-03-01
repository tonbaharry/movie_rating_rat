from django import forms
from django.contrib.auth.models import User
from movie.models import Comment, Movie, UserProfile

class MovieForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the movie name.")
    views = forms.IntegerField()
    likes = forms.IntegerField()
    #releaseYear = forms.DateTimeField(help_text="Please enter the release date")
   # coverPhoto = forms.ImageField(upload_to='movie_images', default='media/profile_images/rango.jpg')
   # trailer = forms.URLField()
    #description = forms.TextInput(attrs={'size': 10, 'title': 'Movie Description',})
    #description = forms.TextInput()

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Movie
    fields = ('likes','views','description')



class CommentForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please add your comment.......")
    #url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    #views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #description = forms.TextInput(attrs={'size': 10, 'title': 'Movie Description',})


    class Meta:
        # Provide an association between the ModelForm and a model
        model = Comment

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign keys
        fields = ('title', 'views')

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    website = forms.URLField(help_text="Please enter your website.", required=False)
    picture = forms.ImageField(help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')