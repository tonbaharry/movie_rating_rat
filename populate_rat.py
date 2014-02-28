import os

def populate():
    horror_cat = add_cat('Horror', views=128, likes=64)

    add_page(cat=horror_cat,
        title="Internet Movie Database",
        url="http://imdb.com")

    add_page(cat=horror_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=horror_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    comedy_cat = add_cat("Comedy", views=64, likes=32)

    add_page(cat=comedy_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=comedy_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=comedy_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    document_cat = add_cat("Document", views=32, likes=16)

    add_page(cat=document_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=document_cat,
        title="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Movie Rat population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating_project.settings')
    from movie.models import Category, Page
    populate()
