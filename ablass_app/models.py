from django.db import models
from django.contrib.auth.models import User

def all_antraege(self):
	return self.antrag_set.all()

User.all_antraege = all_antraege

class Antrag(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	kilometers = models.IntegerField(default=0)
	def tco2(self):
		return '{:.2f}'.format(self.kilometers*0.115)
	def price(self):
		return '{:.2f}'.format(self.kilometers*0.115*180.0)
	def __str__(self):
		return str(self.user)+' absolves himself of '+str(self.kilometers)+'km'