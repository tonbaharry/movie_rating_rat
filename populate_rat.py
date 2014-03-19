import os

def populate():
cmd_mov1 = add_mov('zuma','Zuma is a movie remake of one of the oldest and most popular comic books in the Philippines. It stars Zuma, a creature donning a snake over his shoulder which perfectly accentuates his monster-like features.','Comedy',releaseYear=1985,views=128, likes=64 )

    	comment(mov=cmd_mov1,title='Very credible job',
         description="Kimberly Pierce's take on Carrie puts more emphasis on the bullying aspect of the story",views=4)

    	comment(mov=cmd_mov1,title='Soapy Bravery in Ancient Greece',
    	description="For a remake, it's pretty impressive, and you can't go wrong with a good old Prom scene",views=3)

    	comment(mov=cmd_mov1,title='a super excellent show',
    	description="With great performances from Chloe Grace Moretz and Julianne Moore, Carrie is a great-modern interpretation of Stephen Kings classic novel",views=20)
	
	comment(mov=cmd_mov1,title='Go tell them',
    	description="It is only a vague memory of seeing this film four decades ago, but it impressed me for several reasons",views=12)

	comment(mov=cmd_mov1,title='I like this better than I thought',
    	description="If you enjoy a lot of blood, then watch this",views=26)

act_mov1 = add_mov('Casino Royale','Armed with a license to kill, Secret Agent James Bond sets out on his first mission as 007 and must defeat a weapons dealer in a high stakes game of poker at Casino Royale, but things are not what they seem.','Action',releaseYear=2006,views=582, likes=124 )

    	comment(mov=act_mov1,title='Excellent prequel to the series',
         description=""Casino Royale" is a great re-creation of the series. Cool action, great thrills and a more humane ",views=8)

    	comment(mov=act_mov1,title='Pretentious euro-pudding pseudo-spy movie',
    	description="Other than good performances from Juliette Binoche, Sara Forestier and the likable newcomer Tom Riley, this movie doesn't have much to recommend it.",views=13)

    	comment(mov=act_mov1,title='At last, a good british film!',
    	description="Though it has some flaws, "High tension" is a thoroughly enjoyable and nasty piece of works, with fine acting (kudos to Philippe Nahon as the slimy killer)",views=16)
	
	comment(mov=act_mov1,title='Unabashed fun !',
    	description="The Great bond of darkness is a basic retelling of the "Great Mazinger" series's story : our heroes battle the evil forces of the subterranean Mikene empire",views=12)

	comment(mov=act_mov1,title='Great follow-up to Mazinger',
    	description="I am just speechless",views=65)


act_mov2 = add_mov('American Hustle', 'A con man, Irving Rosenfeld, along with his seductive partner Sydney Prosser, is forced to work for a wild FBI agent, Richie DiMaso, who pushes them into a world of Jersey powerbrokers and mafia. ','Action',releaseYear=2012,views=228, likes=32)
	
	comment(mov=act_mov2,title='Not bad for 40 years ago',
    	description="I was a teenager when I first saw this film. I was raised on the ancient spectacle films of the 50's and 60's and feel this one holds up quite well. No, it's not perfection with respect to history",views=35)
	
	comment(mov=act_mov2,title='My favorite all time movie',
    	description="Seen the movie many times when younger, wanted to get the show again even now",views=21)

	comment(mov=act_mov2,title='A Tale of Courage, Heroism and Idealism',
    	description="A Tale of Courage, Heroism and Idealism.Super excellent",views=47)

	comment(mov=act_mov2,title='A Tale of Courage, Heroism and Idealism',
    	description="A Tale of Courage, Heroism and Idealism.Super excellent",views=47)

act_mov3 = add_mov('Django Unchained', 'With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.','Action',releaseYear=2013,views=46, likes=102)
	
	comment(mov=act_mov3,title='an interesting film about an important world event',
    	description="This film is about the battle of Thermopylae, between the Athenian Democracy and the Persian totalitarian empire.",views=164)

	comment(mov=act_mov3,title='Brilliant!!!',
    	description="Often brilliant essentially-true dramatized history of a great Grecian battle",views=82)

	comment(mov=act_mov3,title='Why isn't this out on VHS let alone DVD?',
    	description="True story of heroic events. AND...it ain't hokey! Must see for any history buff.",views=35)

	comment(mov=act_mov3,title='unforgettable',
    	description="I saw this one many years ago(when it came out) on the big screen. Awesome story. ",views=27)

	comment(mov=act_mov3,title='About par for the course',
    	description="Dimpled German king leads his men to death and glory, while Persian tyrant fumes and stamps his feet.",views=27)

act_mov4 = add_mov('Captain Phillips', 'The true story of Captain Richard Phillips and the 2009 hijacking by Somali pirates of the US-flagged MV Maersk Alabama, the first American cargo ship to be hijacked in two hundred years.','Mystery',releaseYear=2013,views=12, likes=223)	

        
	comment(mov=act_mov4,title='Exhausting, Thrilling and Powerful',
        description="Those little blue people are back in this unfortunate sequel to a terrible children's film.",views=90)

    	comment(mov=act_mov4,title='Orgasmic heights for rock fans, everyone else needn't apply',
        description="YOU WILL KNOW HER NAME",views=4)

    	comment(mov=action_mov,title='Trip's plot doesn't offer more than visual flourishes',
        description="Lacking in thrills and a sluggish build-up, there was so much the filmmakers could have done with this film.",views=10)


commedy_movie = add_mov('fresh prince of belair', 'The Banks family, a respectable Californian family, take in a relative - Will Smith, a street-smart teenager from Philadelphia. The idea is to make him respectable, responsible and mature, but Will has got other plans','comedy',releaseYear=1997,views=807, likes=2066)

    comment(mov=commedy_movie,title='When it's funny, it's hilarious.', description="Sherman Hemsley appeared as two different characters throughout the show, once as Judge Carl Robertson and again later as a cameo playing George Jefferson",views=14)
    comment(mov=commedy_movie, title='When it's lame, it's painful.',description="The living room changed, although they lived in the same house. After they changed it, the stairs were in the living room, they originally weren't there",views=12)
    comment(mov=commedy_movie, title='Entertaining family film that is truly enjoyable',description="For a couple of episodes, the show was entitled 'The Fresh Prince of Philidelphia???' for when Will decided to stay in Philly.",views=10)
    
   


    #Print out what we have added to the user.
    for c in Movie.objects.all():
         for p in Comment.objects.filter(movie=c):
             print "- {0} - {1}".format(str(c), str(p))

def comment(mov,title,description,views=0):
     p = Comment.objects.get_or_create(movie=mov, title=title,description=description,views=views)[0]
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



def add_mov(name,desc,genre,releaseYear=0,views=0,likes=0,):
    c = Movie.objects.get_or_create(name=name,desc=desc,genre=genre,releaseYear=releaseYear,views=views,likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Movie Rat population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_rating_project.settings')
    from movie.models import Movie, Comment
    populate()
