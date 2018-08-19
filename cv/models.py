from django.db import models
from django.utils import timezone


class CVItemType (models.Model):
	typeText = models.TextField();

	def __str__(self):
		return self.typeText


class CVItem (models.Model):
	type = models.ForeignKey('CVItemType', on_delete = models.CASCADE)
	startDate = models.DateField()
	endDate = models.DateField()
	cvTitle = models.TextField(max_length=200)
	cvDescription = models.TextField(max_length=5000)

	def  __str__(self):
		return self.cvTitle

