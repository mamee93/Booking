from django.db import models
from django.utils.timezone import datetime
from  django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
	ROOMTYPE = (
		('Single Room','Single Room'),
		('Single Room','Single Room'),
		('Double Room','Double Room'),
		('VIP Single Room','VIP Single Room'),
		('VIP Double Room','VIP Double Room'),
		)
	ROOM_CONDITION = (
		('Good','Good'),
		('Very Good','Very Good'),
		('Good','Good'),
		('Very Good','Very Good'),

		)
	STATUS_ROOM = (
		('booked up','booked up'),
		('Available','Available'),

		)
	owner     = models.ForeignKey(User,related_name='book_owner', on_delete=models.CASCADE,blank=True, null=True)
	title     = models.CharField(max_length=100)
	room      = models.CharField(max_length=100,choices=ROOMTYPE,null=True)
	content   = models.TextField()
	created   = models.DateTimeField(auto_now_add=True, blank=True)
	updated   = models.DateTimeField(auto_now=True, blank=True)
	post_slug = models.SlugField(blank=True, null=True)
	image     = models.ImageField(upload_to='post/',blank=True, null=True)
	price     = models.FloatField(default=True)
	active    = models.BooleanField(default=False)
	category  = models.ForeignKey('Category',limit_choices_to={'main_category':True},related_name='booking_category', on_delete=models.CASCADE,blank=True,null=True)
	countery  = models.ForeignKey('Countery',limit_choices_to={'main_countery':True},related_name='booking_countery', on_delete=models.CASCADE,blank=True,null=True)
	condition = models.CharField(max_length=15,choices=ROOM_CONDITION,null=True, blank=True)
	status_room = models.CharField(max_length=15,choices = STATUS_ROOM,null=True, blank=True)


	def save(self,*args,**kwargs):
		self.post_slug = self.title
		super(Booking,self).save(*args,**kwargs)

	def __str__(self):
		return self.title

     

class AdImages(models.Model):
    ad =models.ForeignKey(Booking, related_name="ad_images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Booking_images/')


class Category(models.Model):

	name = models.CharField(max_length=50)
	main_category = models.ForeignKey('self',limit_choices_to={'main_category':None},related_name='maincategory', on_delete=models.CASCADE,blank=True,null=True)
     
	def __str__(self):
		return self.name

class Countery(models.Model):

	name = models.CharField(max_length=50)
	main_countery = models.ForeignKey('self',limit_choices_to={'main_countery':None},related_name='maincountery', on_delete=models.CASCADE,blank=True,null=True)
     
	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			('Booked', 'Booked'),
			('No room reservation', 'No room reservation'),
			)
	booking = models.ForeignKey(Booking, null=True, on_delete= models.CASCADE, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.booking.name
