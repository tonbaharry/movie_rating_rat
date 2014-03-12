import os

def populate():
    horror_mov = add_mov('zuma','Zuma is a movie remake of one of the oldest and most popular comic books in the Philippines. It stars Zuma, a creature donning a snake over his shoulder which perfectly accentuates his monster-like features.','Comedy',releaseYear=1985,views=128, likes=64 )

    comment(mov=horror_mov,
         description="Kimberly Pierce's take on Carrie puts more emphasis on the bullying aspect of the story")

    comment(mov=horror_mov,
    description="For a remake, it's pretty impressive, and you can't go wrong with a good old Prom scene")

    comment(mov=horror_mov,
    description="With great performances from Chloe Grace Moretz and Julianne Moore, Carrie is a great-modern interpretation of Stephen Kings classic novel")

    action_mov = add_mov('American Hustle', 'A con man, Irving Rosenfeld, along with his seductive partner Sydney Prosser, is forced to work for a wild FBI agent, Richie DiMaso, who pushes them into a world of Jersey powerbrokers and mafia. ','Action',releaseYear=2012,views=228, likes=32)

    comment(mov=action_mov,
        description="The remake of Carrie, suffers severely from a lead that fails to evoke the same awkward and creepiness")

    comment(mov=action_mov,
        description="YOU WILL KNOW HER NAME")

    comment(mov=action_mov,
        description="Lacking in thrills and a sluggish build-up, there was so much the filmmakers could have done with this film.")

    commedy_movie = add_mov('fresh prince of belair', 'The Banks family, a respectable Californian family, take in a relative - Will Smith, a street-smart teenager from Philadelphia. The idea is to make him respectable, responsible and mature, but Will has got other plans','comedy',releaseYear=1997,views=807, likes=2066)

    comment(mov=commedy_movie, description="Sherman Hemsley appeared as two different characters throughout the show, once as Judge Carl Robertson and again later as a cameo playing George Jefferson")
    comment(mov=commedy_movie, description="The living room changed, although they lived in the same house. After they changed it, the stairs were in the living room, they originally weren't there")
    comment(mov=commedy_movie, description="For a couple of episodes, the show was entitled 'The Fresh Prince of Philidelphia???' for when Will decided to stay in Philly.")
    # Print out what we have added to the user.
    for c in Movie.objects.all():
         for p in Comment.objects.filter(movie=c):
             print "- {0} - {1}".format(str(c), str(p))

def comment(mov,views=0,description):
     p = Comment.objects.get_or_create(movie=mov, description=description)[0]
     return p

def add_mov(name,desc,genre,releaseYear=0,views=0,likes=0,):
    c = Movie.objects.get_or_create(name=name,desc=desc,genre=genre,releaseYear=releaseYear,views=views,likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Movie Rat population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating_project.settings')
    from movie.models import Movie, Comment
    populate()

