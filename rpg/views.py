from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import RequestContext
from django.http import HttpResponse
from django import forms

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html',{'state':state, 'username': username}, context_instance=RequestContext(request))

def index(request):
	title = "My RPG"
	return render_to_response('index.html', {'title':title})

def registration(request):
	state = "Please register."
	username = password = email = ''
	if request.POST:
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		if User.objects.filter(username = username).exists():
			# raise forms.ValidationError("Username %s is already in use." % username)
			state = "Username %s is already in use. Please try another." % username
		else:
			try:
				user = User.objects.create_user(username = username, email = email, password = password)
				state = "Thank you for registering with us %s!" % user.username 
			except:
				state = "Unexpected error occured: %s" % sys.exc_info()[0]

	return render_to_response('registration.html', {'state': state}, context_instance = RequestContext(request))