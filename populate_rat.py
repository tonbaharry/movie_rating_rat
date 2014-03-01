import os

def populate():
    horror_mov = add_mov('Horror','This was a veru funny movie i d like more of this',views=128, likes=64 )

    comment(mov=horror_mov,
         description="This was a veru funny movie i 'd like more of this"
         )

    comment(mov=horror_mov,
    description="This was a veru funny movie i 'd like more of this"
        )



    comedy_mov = add_mov("Comedy", 'This was a veru funny movie i d like more of this',views=128, likes=32)

    comment(mov=comedy_mov,
        description="Official Django Tutorial",
           )

    # add_page(mov=comedy_mov,
    #     movie="Django Rocks",
    #     url="http://www.djangorocks.com/")

    # add_page(mov=comedy_mov,
    #     movie="How to Tango with Django",
    #     url="http://www.tangowithdjango.com/")

    # document_mov = add_mov("Document", views=32, likes=16)

    # add_page(mov=document_mov,
    #     movie="Bottle",
    #     url="http://bottlepy.org/docs/dev/")

    # add_page(mov=document_mov,
    #     movie="Flask",
    #     url="http://flask.pocoo.org")

    # # Print out what we have added to the user.
    # for c in Movie.objects.all():
    #     for p in Comment.objects.filter(movie=c):
    #         print "- {0} - {1}".format(str(c), str(p))

def comment(mov,  description):
     p = Comment.objects.get_or_create(movie=mov, description=description)[0]
     return p

def add_mov(name,desc, views=0, likes=0,):
    c = Movie.objects.get_or_create(name=name,desc=desc,views=views,likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Movie Rat population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating_project.settings')
    from movie.models import Movie, Comment
    populate()
