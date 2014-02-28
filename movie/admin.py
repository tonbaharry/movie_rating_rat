from django.contrib import admin
from movie.models import Movie, Page, UserProfile,MoviePage,Comments

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'movie', 'url')

admin.site.register(Movie)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(MoviePage)
admin.site.register(Comments)
