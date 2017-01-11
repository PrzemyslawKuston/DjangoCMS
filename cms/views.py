from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from notifications.models import Notifications


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

#--- nowe

def login(request):
	c = {}
	return render(request, 'login.html', c)

def auth_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	return render(request, 'loggedin.html',{'user_name' : request.user.username, 'notifications': Notifications.objects.filter(user=request.user, viewed=False)})

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def invalid_login(request):
	return render_to_response('invalid_login.html')

def create_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, '/accounts/create_user_success/')

	args = {}
	args['form'] = UserCreationForm()
	return render(request, 'create_user.html', args)

def create_user_success(request):
	return render(request,'create_user_success.html')
