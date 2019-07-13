from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('info/',views.info,name='info'),
	path('antrag/',views.antrag,name='antrag'),
	path('logbuch/',views.LogbuchListView.as_view(),name='logbuch'),
	path('antrag/ablassen/',views.ablassen,name='ablassen')
]