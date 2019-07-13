from django.db import models

# Create your models here.
class User(models.Model):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	def __str__(self):
		return self.firstname+' '+self.lastname
	def all_children(self):
		return self.antrag_set.all()

class Antrag(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	kilometers = models.IntegerField(default=0)
	def tco2(self):
		return '{:.2f}'.format(self.kilometers*0.115)
	def price(self):
		return '{:.2f}'.format(self.kilometers*0.115*180.0)
	def __str__(self):
		return str(self.user)+' absolves himself of '+str(self.kilometers)+'km'