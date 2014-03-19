import os

def populate():

    comedy_genre = add_gen("Comedy")


    horror_mov = add_mov(gen=comedy_genre,name='About Last Night',
        desc='Follow two couples as they journey from the bar to the bedroom and are eventually put to the test in the real world.',
        releaseYear=2014,
        views=128, 
        likes=1 )

    comment(mov=horror_mov,title='About Last Night',
         description="I cannot get over this remake of a great classic! "+
         "he original was so well acted. Remakes are rarely as good but this "+
         "just plain awful! Aside from Kevin Hart not being funny (ever in anything)...even"+
         " you are someone who thinks he is funny, the acting is still atrocious! Everyone except "+
         "y needs to take acting lessons. They overact (and poorly) to everything they say and do. It"+
         " to the absurd level. If it were that kind of movie, I'd understand - but they took a great movie"+
         "d made a mockery of it. There are so many wonderful and talented black actors out there - why they chose"+
         "s cast is baffling (sans Ealy who is great in everything). I'm just so frustrated by the idea that the younger"+
         "neration will know this movie by this version - tragic for people who appreciate good classics.", 
         ureviewer_name='stephsaddress',   views=4)

    comment(mov=horror_mov,title='This movie will make you laugh out loud.',
    description="kjk",
    ureviewer_name='superwomanproductions',views=3)

    comment(mov=horror_mov,title='Expect it to be average and you  like it',
    description="With great performances from Chloe Grace Moretz and Julianne Moore, Carrie is a"
                " great-modern interpretation of Stephen Kings classic novel",
    ureviewer_name='smokee',
    views=20)

    action_genre = add_gen(
        'Action')

    action_mov = add_mov(gen=action_genre,name='Noah',
                         desc='A man suffering visions of an apocalyptic '
                              'deluge takes measures to protect his family a '
                              'coming flood. Inspired by the Biblical story. ',
                         releaseYear=2014,
                         views=228,
                         likes=32)

    comment(mov=action_mov,title='Good for week end',
        description="The remake of Carrie, suffers severely from a lead that fails"
                    " to evoke the same awkward and creepiness",
        ureviewer_name='smokee',
        views=90)

    comment(mov=action_mov,title='wow',
        description="YOU WILL KNOW HER NAME",
        ureviewer_name='smokee',
        views=4)

    comment(mov=action_mov,title='wow',
        description="Lacking in thrills and a sluggish build-up, "
                    "there was so much the filmmakers could have "
                    "done with this film.",
        ureviewer_name='smokee',
        views=10)

    commedy_movie = add_mov(gen=comedy_genre,
                            name='Divergent',
                            desc='Set in a futuristic dystopia where society is divided into five'
                                 ' factions that each represent a different virtue, teenagers have to '
                                 'decide if they want to stay in their faction or switch to another - for'
                                 ' the rest of their lives. Tris Prior makes a choice that surprises everyone. '
                                 'Then Tris and her fellow faction-members have to live through a highly competitive'
                                 ' initiation process to live out the choice they have made. They must undergo extreme'
                                 ' physical and intense psychological tests, that transform them all. But Tris has a secret'
                                 ' that she is Divergent, which means she doesn\'t fit into any one group. If anyone knew, it'
                                 ' would mean a certain death. As she discovers a growing conflict that threatens to unravel '
                                 'her seemingly perfect society, this secret might help her save the people she loves... '
                                 'or it might destroy her. ',
                            releaseYear=2014,
                            views=807,
                            likes=2066)

    comment(mov=commedy_movie,
            title='Very Futuristic',
            description="Sherman Hemsley appeared as two different "
                        "characters throughout the show, once as Judge C"
                        "arl Robertson and again later as a cameo playing George "
                        "Jefferson",
            ureviewer_name='smokee',
            views=14)
    comment(mov=commedy_movie,
            title='Something that we already seen',
            description="The living room changed, although they"
                        " lived in the same house. After they changed it, the stairs "
                        "were in the living room, they originally weren't there",
            ureviewer_name='smokee',
            views=12)
    comment(mov=commedy_movie,
            title='Not bad',
            description="For a couple of episodes, the show was entitled 'The Fresh Prince "
                        "of Philidelphia???' for when Will decided to stay in Philly.",
            ureviewer_name='smokee',
            views=10)

    mystery_genre = add_gen(
        'Mystery')

    nonstop_movie = add_mov(gen=mystery_genre,
                            name='NonStop',
                            desc='An air marshal springs into action during a transatlantic flight '
                                 'after receiving a series of text messages that put his fellow passengers '
                                 'at risk unless the airline transfers $150 million into an off-shore account.',
                            releaseYear=2014,
                            views=807,
                            likes=2066)

    comment(mov=nonstop_movie,
            title='Great "Edge-Of-Your-Seat" Film',
            description="I saw an advanced screening of this movie yesterday, and I was absolutely blown away. "
                        "I had hoped it would be a fun thrill-ride, but I did not expect "
                        "it to be as exciting and involved as it was.My favorite part of this "
                        "movie, was the fact that it takes a plot that is implausible, and makes "
                        "it as plausible as possible. You can definitely tell that the writers did their "
                        "research on air marshals, airplane mechanics, etc. There was not one moment in this "
                        "film that I was bored, and it was filled to the brim with twists, and turns."
                        "There definitely is a lot that went into this movie, and even though it'll have "
                        "you thinking more deeply about the security of airlines, most of all it's just "
                        "a really, really fun ride.",
            ureviewer_name='Taizpian ',
            views=14)
    comment(mov=nonstop_movie,
            title='Silly as Hell, but quite entertaining',
            description="TAbsolutely ludicrous Liam Neeson thriller (which is a genre now), "
                        "but, frankly, it's just a lot of fun. I found myself smiling and giggling at the silliness "
                        "of it all, but damned if I wasn't enjoying myself the whole time. Neeson plays an air marshal"
                        " who receives a text shortly after his flight commences that, if a load of money isn't "
                        "deposited into an untraceable bank account, a passenger will be killed every 20 minutes. "
                        "The film is clever enough to make it impossible to guess - or, alternatively, you pretty "
                        "much suspect everyone and hope like Hell they don't pull out the old Liam-Neeson-has-"
                        "multiple-personalities-and-is-doing-it-himself twist. The film is hilariously convoluted "
                        "with plenty of plot holes. When the villain is revealed, they say 'You'd never believe "
                        "how easy it all was!' "
                        "They are correct. "
                        " I would never believe it. I still quite enjoyed watching it.",
            ureviewer_name='zetes',
            views=12)
    comment(mov=nonstop_movie,
            title='awesome action movie',
            description="'Non-Stop' is an action mystery thriller starring Liam Neeson"
                        " and Julianne Moore and is directed by Jaume Collet-Serra (Unknown, Orphan)."
                        " The story takes place 30,000 feet above the Atlantic Ocean inside of a plane traveling "
                        "from New York to London. Bill (Liam Neeson) is a Federal Air Marshall with a troubled past."
                        " He is assigned to accompany the international flight when things take a turn for the "
                        "worst and there is an apparent hijacking of the plane. The catch: Bill is being framed."
                        " Don't worry though, I haven't spoiled anything you couldn't find in the trailer already."
                        " But, while it might sound like you have heard this plot "
                                  "100 times before just in different settings, you may be in fact incorrect.",
            ureviewer_name='renton Hoshiko',
            views=10)


    thriller_genre = add_gen(
        'Thriller')

    tournament_movie = add_mov(gen=thriller_genre,
                            name='Tournament',
                            desc='Every seven years in an unsuspecting town, The Tournament takes place. '
                                 'A battle royale between 30 of the world\'s deadliest assassins. '
                                 'The last man standing receiving the $10,000,000 cash prize '
                                 'and the title of Worlds No 1, which itself carries the legendary '
                                 'million dollar a bullet price tag. ',
                            releaseYear=2009,
                            views=807,
                            likes=2066)

    comment(mov=tournament_movie,
            title='Believe me, Middlesborough never',
            description="I saw an advanced screening of this movie yesterday, and I was absolutely blown away. "
                        "I had hoped it would be a fun thrill-ride, but I did not expect "
                        "it to be as exciting and involved as it was.My favorite part of this "
                        "movie, was the fact that it takes a plot that is implausible, and makes "
                        "it as plausible as possible. You can definitely tell that the writers did their "
                        "research on air marshals, airplane mechanics, etc. There was not one moment in this "
                        "film that I was bored, and it was filled to the brim with twists, and turns."
                        "There definitely is a lot that went into this movie, and even though it'll have "
                        "you thinking more deeply about the security of airlines, most of all it's just "
                        "a really, really fun ride.",
            ureviewer_name='Taizpian ',
            views=14)
    comment(mov=nonstop_movie,
            title='Silly as Hell, but quite entertaining',
            description="TAbsolutely ludicrous Liam Neeson thriller (which is a genre now), "
                        "but, frankly, it's just a lot of fun. I found myself smiling and giggling at the silliness "
                        "of it all, but damned if I wasn't enjoying myself the whole time. Neeson plays an air marshal"
                        " who receives a text shortly after his flight commences that, if a load of money isn't "
                        "deposited into an untraceable bank account, a passenger will be killed every 20 minutes. "
                        "The film is clever enough to make it impossible to guess - or, alternatively, you pretty "
                        "much suspect everyone and hope like Hell they don't pull out the old Liam-Neeson-has-"
                        "multiple-personalities-and-is-doing-it-himself twist. The film is hilariously convoluted "
                        "with plenty of plot holes. When the villain is revealed, they say 'You'd never believe "
                        "how easy it all was!' "
                        "They are correct."
                        " I would never believe it. I still quite enjoyed watching it.",
            ureviewer_name='zetes',
            views=12)
    comment(mov=nonstop_movie,
            title='awesome action movie',
            description="'Non-Stop' is an action mystery thriller starring Liam Neeson"
                        " and Julianne Moore and is directed by Jaume Collet-Serra (Unknown, Orphan)."
                        " The story takes place 30,000 feet above the Atlantic Ocean inside of a plane traveling "
                        "from New York to London. Bill (Liam Neeson) is a Federal Air Marshall with a troubled past."
                        " He is assigned to accompany the international flight when things take a turn for the "
                        "worst and there is an apparent hijacking of the plane. The catch: Bill is being framed."
                        " Don't worry though, I haven't spoiled anything you couldn't find in the trailer already."
                        " But, while it might sound like you have heard this plot "
                                  "100 times before just in different settings, you may be in fact incorrect.",
            ureviewer_name='renton Hoshiko',
            views=10)
   


    
    #Print out what we have added to the user.
    for a in Genre.objects.all():
        for c in Movie.objects.all():
            for p in Comment.objects.filter(movie=c):
                 print "- {0} - {1}".format(str(c), str(p), str(a))

def add_gen(name):
    a = Genre.objects.get_or_create(name=name)[0]
    return a

def comment(mov,title,description,ureviewer_name,views=0):
     p = Comment.objects.get_or_create(movie=mov, title=title,description=description,ureviewer_name=ureviewer_name,views=views)[0]
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

