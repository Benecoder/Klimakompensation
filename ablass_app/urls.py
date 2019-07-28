from django.urls import path
from . import views

urlpatterns = [
	path("" ,views.index,name='index'),
	path('info/',views.info,name='info'),
	path('antrag/',views.antrag,name='antrag'),
	path('login_page/',views.login_page,name='login_page'),
	path('login_request/',views.login_request,name='login_request'),
	path('logout_request/',views.logout_request,name='logout_request'),
	path('logbuch/',views.LogbuchListView.as_view(),name='logbuch'),
	path('antrag/ablassen/',views.ablassen,name='ablassen'),
	path('load_image/',views.load_image,name='load_image')
]
