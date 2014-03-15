import os

def populate():

    comedy_genre = add_gen("Comedy")


    horror_mov = add_mov(gen=comedy_genre,name='zuma',desc='Zuma is a movie remake of one of the oldest and most popular comic books in the Philippines. It stars Zuma, a creature donning a snake over his shoulder which perfectly accentuates his monster-like features.',releaseYear=1985,views=128, likes=64 )

    comment(mov=horror_mov,title='wow',
         description="Kimberly Pierce's take on Carrie puts more emphasis on the bullying aspect of the story",views=4)

    comment(mov=horror_mov,title='wow',
    description="For a remake, it's pretty impressive, and you can't go wrong with a good old Prom scene",views=3)

    comment(mov=horror_mov,title='wow',
    description="With great performances from Chloe Grace Moretz and Julianne Moore, Carrie is a great-modern interpretation of Stephen Kings classic novel",views=20)

    action_genre = add_gen(
        'Action')

    action_mov = add_mov(gen=action_genre,name='American Hustle', desc='A con man, Irving Rosenfeld, along with his seductive partner Sydney Prosser, is forced to work for a wild FBI agent, Richie DiMaso, who pushes them into a world of Jersey powerbrokers and mafia. ',releaseYear=2012,views=228, likes=32)

    comment(mov=action_mov,title='wow',
        description="The remake of Carrie, suffers severely from a lead that fails to evoke the same awkward and creepiness",views=90)

    comment(mov=action_mov,title='wow',
        description="YOU WILL KNOW HER NAME",views=4)

    comment(mov=action_mov,title='wow',
        description="Lacking in thrills and a sluggish build-up, there was so much the filmmakers could have done with this film.",views=10)

    commedy_movie = add_mov(gen=comedy_genre,name='fresh prince of belair', desc='The Banks family, a respectable Californian family, take in a relative - Will Smith, a street-smart teenager from Philadelphia. The idea is to make him respectable, responsible and mature, but Will has got other plans',releaseYear=1997,views=807, likes=2066)

    comment(mov=commedy_movie,title='wow', description="Sherman Hemsley appeared as two different characters throughout the show, once as Judge Carl Robertson and again later as a cameo playing George Jefferson",views=14)
    comment(mov=commedy_movie, title='wow',description="The living room changed, although they lived in the same house. After they changed it, the stairs were in the living room, they originally weren't there",views=12)
    comment(mov=commedy_movie, title='wow',description="For a couple of episodes, the show was entitled 'The Fresh Prince of Philidelphia???' for when Will decided to stay in Philly.",views=10)
    
   


    #Print out what we have added to the user.
    for c in Movie.objects.all():
         for p in Comment.objects.filter(movie=c):
             print "- {0} - {1}".format(str(c), str(p))

def add_gen(name):
    a = Genre.objects.get_or_create(name=name)[0]
    return a

def comment(mov,title,description,views=0):
     p = Comment.objects.get_or_create(movie=mov, title=title,description=description,views=views)[0]
     return p


def add_mov(gen,name,desc,releaseYear=0,views=0,likes=0,):
    c = Movie.objects.get_or_create(genre=gen,name=name,desc=desc,releaseYear=releaseYear,views=views,likes=likes)[0]
    return c



# Start execution here!
if __name__ == '__main__':
    print "Starting Movie Rat population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating_project.settings')
    from movie.models import Movie, Comment,Genre
    populate()

