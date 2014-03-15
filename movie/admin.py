from django.contrib import admin
from movie.models import Movie, Comment, UserProfile,Genre

class PageAdmin(admin.ModelAdmin):
	list_display = ( )
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(UserProfile)

