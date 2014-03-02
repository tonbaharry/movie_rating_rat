import os

def populate():
    horror_mov = add_mov('zuma','This was a veru funny movie i d like more of this','Comedy',releaseYear=1930,views=128, likes=64 )

    comment(mov=horror_mov,
         description="This was a veru funny movie i 'd like more of this"
         )

    comment(mov=horror_mov,
    description="This was a veru funny movie i 'd like more of this"
        )



    comedy_mov = add_mov("Comedy", 'This was a veru funny movie i d like more of this','Document',releaseYear=2012,views=128, likes=32)

    comment(mov=comedy_mov,
        description="Official Django Tutorial",
           )



    # Print out what we have added to the user.
    for c in Movie.objects.all():
         for p in Comment.objects.filter(movie=c):
             print "- {0} - {1}".format(str(c), str(p))

def comment(mov,  description):
     p = Comment.objects.get_or_create(movie=mov, description=description)[0]
     return p

def add_mov(name,desc,genre ,releaseYear=0,views=0, likes=0,):
    c = Movie.objects.get_or_create(name=name,desc=desc,genre=genre,releaseYear=releaseYear,views=views,likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Movie Rat population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating_project.settings')
    from movie.models import Movie, Comment
    populate()
