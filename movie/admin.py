from django.contrib import admin
from movie.models import Category, Page, UserProfile, Movie,MoviePage,Comments

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
admin.site.register(MoviePage)
admin.site.register(Movie)
admin.site.register(Comments)
