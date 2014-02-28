from django.contrib import admin
from movie.models import Movie, Comment, UserProfile

class PageAdmin(admin.ModelAdmin):
	list_display = ( )

admin.site.register(Movie)
admin.site.register(Comment, PageAdmin)
admin.site.register(UserProfile)
#admin.site.register(Comments)
