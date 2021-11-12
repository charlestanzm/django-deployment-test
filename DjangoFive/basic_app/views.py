from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm
# Create your views here.

# A lot of coding for working with Users and Authorization is in this file 
# Sometimes, want to save information directly to databases 
# Other times, we want to manipulate the data a little bit before saving it
    # set commit = False 
    # helps prevent collision errors 


def index(request):
    return render(request, 'basic_app/index.html') 


def register(request):
    
    registered = False 

    if request.method == "POST":
        user_form = UserForm(data = request.POST) 
        profile_form = UserProfileInfoForm(data = request.POST) 

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save() 
            user.set_password(user.password) # hashes the password 
            user.save() # commit the entry to the database (for fields of the admin User model)

            profile = profile_form.save(commit = False) # do not commit to database yet. 
            profile.user = user # linking this input 

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save() 
            registered = True 

        else: 
            print(user_form.errors, profile_form.errors) # displays the errors made in the forms 
        
    else: 
        user_form = UserForm() 
        profile_form = UserProfileInfoForm() 

    return render(request, 'basic_app/registration.html',
                        {'user_form':user_form,
                        'profile_form':profile_form,
                        'registered':registered})


# For login and logout functions, need a lot of django functionalities 
    # one of the key logic to include is to show "logout" button when logged in, and vice versa 

from django.urls import reverse
from django.contrib.auth.decorators import login_required
    # a decorator that requires a logged in account to access a particular view
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def user_login(request): 

    if request.method == 'POST': # if someone has submitted a login request,
        username = request.POST.get('username') # this 'username' comes from the name = 'username' in the html
        password = request.POST.get('password') 

        user = authenticate(username = username, password = password) 
            # Django automatically authenticates that user (no additional code required) 

        if user: 
            if user.is_active: 
                login(request, user) 
                return HttpResponseRedirect(reverse('index')) # after login successful, redirects them back to homepage 
            else: 
                return HttpResponseRedirect('Invalid account/password') 
        
        else: 
            print("Someone tried to login and failed") 
            print("Username:{} and passowrd{}".format(username, password))
            return HttpResponse('Invalid Login') 

    else: 
        return render(request, 'basic_app/login.html', {})

@login_required
def special(request): 
    return HttpResponse("You are logged in") 


@login_required
def user_logout(request): 
    logout(request) 
    return HttpResponseRedirect(reverse('index')) 