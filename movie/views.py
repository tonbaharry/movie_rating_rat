from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from movie.models import Genre
from movie.models import Movie
from movie.models import Comment
from movie.models import UserProfile
from movie.forms import UserForm, UserProfileForm
from movie.forms import MovieForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from movie.bing_search import run_query
from django.contrib.auth.models import User
from django.shortcuts import redirect


def encode_url(str):
    return str.replace(' ', '_')


def decode_url(str):
    return str.replace('_', ' ')


def get_movie_list(max_results=0, starts_with=''):
    mov_list = []
    if starts_with:
        mov_list = Movie.objects.filter(name__istartswith=starts_with)
    else:
        mov_list = Movie.objects.all()

    if max_results > 0:
        if (len(mov_list) > max_results):
            mov_list = mov_list[:max_results]

    for mov in mov_list:
        mov.url = encode_url(mov.name)

    return mov_list

    for movin in com_list:
        mov.url = encode_url(mov.name)

    return mov_list

def get_worst_movie_list(max_results=0, starts_with=''):
    worst_mov_list = []
    if starts_with:
        worst_mov_list = Movie.objects.filter(name__istartswith=starts_with)
    else:
        worst_mov_list = Movie.objects.all()

    if max_results > 0:
        if (len(worst_mov_list) > max_results):
            worst_mov_list = worst_mov_list[:max_results]

    for worst_mov in worst_mov_list:
        worst_mov.url = encode_url(worst_mov.name)

    return worst_mov_list

    for worst_movin in worst_com_list:
        worst_cmov.url = encode_url(mov.name)

    return worst_mov_list


def index(request):
    context = RequestContext(request)


#------------------------------------------------------------------

    top_movie_list = Movie.objects.order_by('-likes')[:5]
    

    for movie in top_movie_list:
        movie.url = encode_url(movie.name)

    context_dict = {'movie': top_movie_list}

    mov_list = get_movie_list()
    context_dict['mov_list'] = mov_list
#-------------------------------------------------------------------

    movi_list = Movie.objects.order_by('likes')[:5]
    

    for movie in movi_list:
        movie.url = encode_url(movie.name)

    context_dictr = {'movi': movi_list}
    context_dict['movi'] = movi_list

#-----------------------------------------------------------
    
    comment_list = Comment.objects.order_by('-views')[:5]
    
    for comment in comment_list:
        comment.url = comment.movie.name.replace(' ', '_')
    
    context_dictr = {'comments': comment_list}
    context_dict['comments'] = comment_list



#-------------------------------------------------------
    genre_list = Genre.objects.all()
    context_dict['genres']=  genre_list




    if request.session.get('last_visit'):
    # The session has a value for the last visit
        last_visit_time = request.session.get('last_visit')

        visits = request.session.get('visits', 0)

        if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).days > 0:
            request.session['visits'] = visits + 1
    else:
        # The get returns None, and the session does not have a value for the last visit.
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = 1
    return render_to_response('movie/index.html', context_dict, context)
    #----------------------------------------------------
def genre(request, genre_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the category name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    genre_name = decode_url(genre_name_url)
    context_dict = {'genre_name': genre_name, 'genre_name_url': genre_name_url}
    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the category passed by the user.
    context_dict = {'genre_name': genre_name}

    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        genre = Genre.objects.get(name=genre_name)

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        movie = Movie.objects.filter(genre=genre)

        # Adds our results list to the template context under name pages.
        context_dict['movie'] = movie
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['genre'] = genre
    except Genre.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('movie/genre.html', context_dict, context)


def about(request):
    # Request the context.
    context = RequestContext(request)
    context_dict = {}
    mov_list = get_movie_list()
    context_dict['mov_list'] = mov_list
    # If the visits session varible exists, take it and use it.
    # If it doesn't, we haven't visited the site so set the count to zero.

    count = request.session.get('visits', 0)

    context_dict['visit_count'] = count

    # Return and render the response, ensuring the count is passed to the template engine.
    return render_to_response('movie/about.html', context_dict, context)

    #-------------------------------------------------------------------------------------------------
def movie(request, movie_name_url):

    context = RequestContext(request)


    movie_name = decode_url(movie_name_url)

    # Build up the dictionary we will use as out template context dictionary.
    context_dict = {'movie_name': movie_name, 'movie_name_url': movie_name_url}

    mov_list = get_movie_list()
    context_dict['mov_list'] = mov_list

    try:
        # Find the movie with the given name.
        # Raises an exception if the movie doesn't exist.
        # We also do a case insensitive match.
        movie = Movie.objects.get(name__iexact=movie_name)
        context_dict['movie'] = movie
        # Retrieve all the associated pages.
        # Note that filter returns >= 1 model instance.
        comments = Comment.objects.filter(movie=movie).order_by('-views')

        # Adds our results list to the template context under name pages.
        context_dict['comments'] = comments
    except Movie.DoesNotExist:
        # We get here if the movie does not exist.
        # Will trigger the template to display the 'no category' message.
        pass

    if request.method == 'POST':
        query = request.POST.get('query')
        if query:
            query = query.strip()
            result_list = run_query(query)
            context_dict['result_list'] = result_list

    # Go render the response and return it to the client.
    return render_to_response('movie/movie.html', context_dict, context)
#------------------------------------------------------------------------------------------

@login_required
def add_movie(request):
    # Get the context from the request.
    context = RequestContext(request)
    mov_list = get_movie_list()
    context_dict = {}
    context_dict['mov_list'] = mov_list

    # A HTTP POST?
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new movie to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
        # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = MovieForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    context_dict['form'] = form
    return render_to_response('movie/add_movie.html', context_dict, context)



@login_required
def add_comments(request, movie_name_url):
    context = RequestContext(request)
    mov_list = get_movie_list()
    context_dict = {}
    context_dict['mov_list'] = mov_list

    movie_name = decode_url(movie_name_url)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            comment = form.save(commit=False)

            # Retrieve the associated Category object so we can add it.
            try:
                mov = Movie.objects.get(name=movie_name)
                comment.movie = mov
            except Movie.DoesNotExist:
                return render_to_response('movie/add_comment.html',
                                          context_dict,
                                          context)

            # Also, create a default value for the number of views.
            comment.views = 0


            # With this, we can then save our new model instance.
            comment.save()

            # Now that the page is saved, display the category instead.
            return movie(request, movie_name_url)
        else:
            print form.errors
    else:
        form = CommentForm()

    context_dict['movie_name_url'] = movie_name_url
    context_dict['movie_name'] = movie_name
    context_dict['form'] = form

    return render_to_response('movie/add_comment.html',
                              context_dict,
                              context)


def register(request):
    # Request the context.
    context = RequestContext(request)
    mov_list = get_movie_list()
    context_dict = {}
    context_dict['mov_list'] = mov_list
    # Boolean telling us whether registration was successful or not.
    # Initially False; presume it was a failure until proven otherwise!
    registered = False

    # If HTTP POST, we wish to process form data and create an account.
    if request.method == 'POST':
        # Grab raw form data - making use of both FormModels.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Two valid forms?
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data. That one is easy.
            user = user_form.save()

            # Now a user account exists, we hash the password with the set_password() method.
            # Then we can update the account with .save().
            user.set_password(user.password)
            user.save()

            # Now we can sort out the UserProfile instance.
            # We'll be setting values for the instance ourselves, so commit=False prevents Django from saving the instance automatically.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Profile picture supplied? If so, we put it in the new UserProfile.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the model instance!
            profile.save()

            # We can say registration was successful.
            registered = True

        # Invalid form(s) - just print errors to the terminal.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render the two ModelForms to allow a user to input their data.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context_dict['user_form'] = user_form
    context_dict['profile_form'] = profile_form
    context_dict['registered'] = registered

    # Render and return!
    return render_to_response(
        'movie/register.html',
        context_dict,
        context)


def user_login(request):
    # Obtain our request's context.
    context = RequestContext(request)
    mov_list = get_movie_list()
    context_dict = {}
    context_dict['mov_list'] = mov_list

    # If HTTP POST, pull out form data and process it.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Attempt to log the user in with the supplied credentials.
        # A User object is returned if correct - None if not.
        user = authenticate(username=username, password=password)

        # A valid user logged in?
        if user is not None:
            # Check if the account is active (can be used).
            # If so, log the user in and redirect them to the homepage.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/movie/')
            # The account is inactive; tell by adding variable to the template context.
            else:
                context_dict['disabled_account'] = True
                return render_to_response('movie/login.html', context_dict, context)
        # Invalid login details supplied!
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            context_dict['bad_details'] = True
            return render_to_response('movie/login.html', context_dict, context)

    # Not a HTTP POST - most likely a HTTP GET. In this case, we render the login form for the user.
    else:
        return render_to_response('movie/login.html', context_dict, context)


@login_required
def restricted(request):
    context = RequestContext(request)
    
    mov_list = get_movie_list()
    context_dict = {}
    context_dict['mov_list'] = mov_list
    return render_to_response('movie/restricted.html', context_dict, context)

# Only allow logged in users to logout - add the @login_required decorator!
@login_required
def user_logout(request):
    # As we can assume the user is logged in, we can just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/movie/')


def search(request):
    context = RequestContext(request)

    mov_list = get_movie_list()
    context_dict = {}
    context_dict['mov_list'] = mov_list

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    context_dict['result_list'] = result_list
    return render_to_response('movie/search.html', context_dict, context)


@login_required
def profile(request):
    context = RequestContext(request)
    mov_list = get_movie_list()
    context_dict = {'mov_list': mov_list}
    u = User.objects.get(username=request.user)

    try:
        up = UserProfile.objects.get(user=u)
    except:
        up = None

    context_dict['user'] = u
    context_dict['userprofile'] = up
    return render_to_response('movie/profile.html', context_dict, context)





@login_required
def like_movie(request):
    context = RequestContext(request)
    mov_id = None
    if request.method == 'GET':
        mov_id = request.GET['movie_id']

    likes = 0
    if mov_id:
        movie = Movie.objects.get(id=int(mov_id))
        if movie:
            likes = movie.likes + 1
        movie.likes = likes
        movie.save()

    return HttpResponse(likes)
def track_url(request):
    context = RequestContext(request)
    comment_id = None
    url = '/movie/'
    if request.method == 'GET':
        if 'comment_id' in request.GET:
            comment_id = request.GET['comment_id']
            try:
                comment = Comment.objects.get(id=comment_id)
                comment.views = comment.views + 1
                comment.save()
                url = comment.url
            except:
                pass

    return redirect(url)



def suggest_movie(request):
    context = RequestContext(request)
    mov_list = []
    starts_with = ''
    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    else:
        starts_with = request.POST['suggestion']

    mov_list = get_movie_list(8, starts_with)

    return render_to_response('movie/movie_list.html', {'mov_list': mov_list}, context)


@login_required
def auto_comments(request):
    context = RequestContext(request)
    mov_id = None
    url = None
    title = None
    context_dict = {}
    if request.method == 'GET':
        mov_id = request.GET['movie_id']
        url = request.GET['url']
        title = request.GET['title']
        if mov_id:
            movie = Movie.objects.get(id=int(mov_id))
            p = Comment.objects.get_or_create(movie=movie, title=title, url=url)

            movies = Comment.objects.filter(movie=movie).order_by('-views')

            # Adds our results list to the template context under name pages.
            context_dict['movies'] = movies

    return render_to_response('movie/page_list.html', context_dict, context)






#---------------------------------------------------
