from __future__ import unicode_literals

from django.db import models

# Create your models here.
def upload_location(instance,filename):
	return "{0}/{1}/PaymentSnapshot/{2}".format(instance.owner,instance.account_number,filename)
	

class Subscriber(models.Model):
	GenderChoices = (
		('M', 'Male'),
		('F', 'Female')
		)
	first_name = models.CharField(max_length=20, default='',blank=False,null=False)
	last_name = models.CharField(max_length=20, default='',blank=False,null=False)
	sex = models.CharField(max_length=1, choices=GenderChoices, null=False, default='M')
	phone_number = models.CharField(max_length=11, default='', null=False, blank=True)
	email = models.CharField(max_length=30, default='', null=False, blank=False)
	Address = models.CharField(max_length=100, default='', null=False, blank=False)
	country = models.CharField(max_length=50, default='', null=False, blank=False)
	state = models.CharField(max_length=50, default='', null=False, blank=False)
	city = models.CharField(max_length=50, default='',null=False, blank=False)

	def __unicode__(self):
		return self.email

	def __str__(self):
		return self.email

class PaymentDetail(models.Model):
	PAYMENT_MEANS_CHOICE = (
		('B','Bank Deposit'),
		('A','ATM Transfer'),
		('M','Mobile Transfer'),
	)
	owner = models.OneToOneField(Subscriber)
	account_number = models.CharField(max_length=30, default='', null=False, blank=False)
	account_name = models.CharField(max_length=60, default='', null=False, blank=False)
	bank_name = models.CharField(max_length=30, default='', null=False, blank=False)
	payment_means = models.CharField(max_length=5, choices=PAYMENT_MEANS_CHOICE, default='B', null=False, blank=False)
	payment_snapshot = models.ImageField(upload_to=upload_location,null=True, blank=True,height_field="img_height", width_field="img_width")


	def __unicode__(self):
		return self.account_number

	def __str__(self):
		return self.account_number