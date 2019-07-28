from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.views.generic.list import ListView
from django.templatetags.static import static
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.models import User
from .models import Antrag

# Create your views here.
def index(request):
	"""
	View for the home page
	"""
	return render(request,'home.html',{})


def info(request):
	"""
	View for the info page
	"""
	return render(request,'info.html')

def antrag(request):
	"""
	View for the ablass form
	"""
	return render(request,'antrag.html')

def login_page(request):
	"""
	View for the login
	"""
	return render(request,'login.html')

def login_request(request):
	u_name = request.POST.get('username')
	p_word = request.POST.get('password')

	user = authenticate(request,username=u_name,password=p_word)
	if user is not None:
		login(request,user)
		return HttpResponseRedirect(reverse('index'))
	else:
		return HttpResponseRedirect(reverse('login_request'))

def logout_request(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def ablassen(request):
	"""
	Handels ablass forms
	"""
	kilometers = request.POST.get('kilometers',False)

	#creates the Antrag object
	new_antrag = Antrag(user = request.user,kilometers= int(kilometers))
	new_antrag.save()


	return HttpResponseRedirect(reverse('logbuch'))

class LogbuchListView(ListView):
	"""
	zeichnet das logbuch auf
	"""
	model = User
	template_name = 'logbuch.html'

	def get_context_data(self):
		context = super().get_context_data()
		return context


def load_image(request):

	type = request.GET.get('type',None)
	if type == 'before':
		data = {'url':static('images/before.jpg')}
	if type == 'after':
		data = {'url':static('images/after.jpg')}
	return JsonResponse(data)

