from __future__ import unicode_literals

from django.db import models

# Create your models here.
		
class Building(models.Model):
	def __unicode__(self):
		return self.Building_Name
	Building_Name = models.CharField(max_length = 8)

class BuildingImage(models.Model):
	building = models.ForeignKey(Building)
	def __unicode__(self):
		return ''
	image = models.ImageField()

class Information(models.Model):
	Index = models.IntegerField(blank = True, null = True)
	Building_option = models.ManyToManyField(Building)
	# Building_option = models.CharField(max_length = 6)
	Room = models.IntegerField()
	Desk = models.CharField(max_length = 6)
	Extension = models.IntegerField(blank = True, null = True)
	UWID = models.IntegerField()
	Email = models.EmailField(blank = True, null = True)
	Last_Name = models.CharField(max_length = 15)
	First_Name = models.CharField(max_length = 15)
	Status = models.CharField(max_length = 6)
	First_Supervisor = models.CharField(max_length = 20)
	Second_Supervisor = models.CharField(blank = True, max_length = 20)
	Third_Supervisor = models.CharField(blank = True, max_length = 20)
	Start_Date = models.DateField()
	End_Date = models.DateField()
	FOB = models.BooleanField(default = False)
	FOB_pu = models.BooleanField(default = False)
	Added_to_existing_FOB = models.BooleanField(default = False)
	def __unicode__(self):
		return self.First_Name+' '+self.Last_Name