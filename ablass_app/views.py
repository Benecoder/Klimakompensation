from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.views.generic.list import ListView
from django.templatetags.static import static


from .models import User,Antrag

# Create your views here.
def index(request):
	"""
	View for the home page
	"""
	return render(request,'home.html')


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

def ablassen(request):
	"""
	Handels ablass forms
	"""
	firstname = request.POST.get('firstname',False)
	lastname = request.POST.get('lastname',False)
	kilometers = request.POST.get('kilometers',False)

	# finds the matching user
	matches = User.objects.filter(firstname=firstname,lastname=lastname)
	if len(matches) == 0:
		user = User(firstname=firstname,lastname=lastname)
		user.save()
	else:
		user = matches.first()

	#creates the Antrag object
	new_antrag = Antrag(user = user,kilometers= int(kilometers))
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

