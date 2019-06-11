from django.db import models

class Event(models.Model):
	name = models.CharField('Event Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.CharField(max_length=120)
	manager = models.CharField(max_length = 60)
	description = models.TextField(blank=True)

class race(models.Model):
	track = models.CharField('Track', max_length=120)
	laps = models.CharField('laps', max_length=120)
