import os

def populate():
    horror_mov = add_mov('Horror', views=128, likes=64)

    add_page(mov=horror_mov,
        title="Internet Movie Database",
        url="http://imdb.com")

    add_page(mov=horror_mov,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(mov=horror_mov,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    comedy_mov = add_mov("Comedy", views=64, likes=32)

    add_page(mov=comedy_mov,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(mov=comedy_mov,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(mov=comedy_mov,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    document_mov = add_mov("Document", views=32, likes=16)

    add_page(mov=document_mov,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(mov=document_mov,
        title="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Movie.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(mov, title, url, views=0):
    p = Page.objects.get_or_create(category=mov, title=title, url=url, views=views)[0]
    return p

def add_mov(name, views=0, likes=0):
    c = Movie.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Movie Rat population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating_project.settings')
    from movie.models import Movie, Page
    populate()
