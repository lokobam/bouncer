from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.
from .forms import RegisterForm,ContactForm
from .models import Subscriber


class HomeTemplateView(TemplateView):
	template_name = 'index.html'
	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		context['title'] = 'welcome to fsrst'

		return context



class AboutTemplateView(TemplateView):
	template_name = 'about.html'
	def get_context_data(self, **kwargs):
		context = super(AboutTemplateView, self).get_context_data(**kwargs)
		context['title'] = 'About'

		return context

def register_view(request):
	register = RegisterForm(request.POST or None,request.FILES or None)

	if register.is_valid():
		instance = register.save(commit=False)
		instance.save()
		return redirect('/')

	context = {
		'form' : register,
	}

	return render(request, 'register.html', context)

def contact_view(request):
    title_align_center=False
    title='contact us'
    form=ContactForm(request.POST or None)
    if form.is_valid():
        #METHOD 1
        #for key,value in form.cleaned_data.iteritems():
        #   print key +' : '+ value
        #METHOD 2
        #for key in form.cleaned_data:
        #    print key,form.cleaned_data.get(key)
        #METHOD 3
        #getting the data from the form fields
        form_name=form.cleaned_data.get("name")
        form_email=form.cleaned_data.get("email")
        form_phone_number=form.cleaned_data.get("phone_number")
        form_message=form.cleaned_data.get("message")
        
        #setting the parameters for the sendmail function
        subject='site contact form'
        contact_message='{0} {1} via {2}'.format(form_name,
        					form_message,
        					form_email
        					)
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email,'akinbamidayo@yahoo.com'] #this is field is a list
        #calling the send_mail function
        send_mail(subject,
        	contact_message,
        	from_email,
        	to_email,
        	fail_silently=False
        	)
        #print form.cleaned_data,email,name,phone_number,message
    context={
    	'form':form,
    	'title':title,
    	'title_align_center':title_align_center,
    
    }
    return render(request,'contact.html',context)