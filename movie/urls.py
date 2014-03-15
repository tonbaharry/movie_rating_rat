from django.conf.urls import patterns, url
from movie import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^movie/(?P<movie_name_url>\w+)/$', views.movie, name='movie'),
	url(r'^add_movie/$', views.add_movie, name='add_movie'),
	url(r'^movie/(?P<movie_name_url>\w+)/comment/$', views.add_comments, name='comments'),
    url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/$', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^search/$', views.search, name='search'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^goto/$', views.track_url, name='track_url'),
    url(r'^like_movie/$', views.like_movie, name='like_movie'),
    url(r'^suggest_movie/$', views.suggest_movie, name='suggest_movie'),
    url(r'^auto_comments/$', views.auto_comments, name='auto_comments'),
    url(r'^genre/(?P<genre_name_url>\w+)/$', views.genre, name='genre'),
	)

