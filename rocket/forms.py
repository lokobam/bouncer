from django import forms
from .models import Subscriber



class ContactForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Name", 'type': 'text', 'name':"name"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Phone Number", 'type': 'text', 'name':"phone_number"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':"Type your message here...", 'rows':'9', 'type': 'text', 'name':"phone_number"}))

class RegisterForm(forms.ModelForm):
	GenderChoices = (
		('M', 'Male'),
		('F', 'Female')
		)
	first_name =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"First Name", 'type': 'text', 'name':"first_name"}))
	last_name =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Last Name", 'type': 'text', 'name':"last_name"}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"type":"email","placeholder":"Email", "name":"email"}))
	sex = forms.ChoiceField(widget=forms.RadioSelect(attrs={'name':"option-yes"}),choices=GenderChoices)
	phone_number =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Phone Number", 'type': 'text', 'name':"phone_number"}))
	Address =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Address", 'type': 'text', 'name':"Address"}))
	country =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"Country", 'type': 'text', 'name':"country"}))
	state =  forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':"State", 'type': 'text', 'name':"state"}))

	class Meta:
		model = Subscriber
		fields = [
			'first_name',
			'last_name',
			'sex',
			'phone_number',
			'email',
			'Address',
			'country',
			'state',
			'city',

		]

	def clean_email(self):
		email = self.cleaned_data.get('email')

		email_qs = Subscriber.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError('This email is already registered')

		return email

