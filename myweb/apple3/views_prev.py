# Create your views here.
from apple3.forms import *
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext,loader
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from apple3.models import Person,Input
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q


def index(request):
    	user=request.user
    	if user.is_anonymous:
		a=0
	if request.user.is_active and request.user.is_authenticated:
		a=1
		   	
    	template=loader.get_template('apple3/index.html')
	context=RequestContext(request,{
			'a':a,
		}
		)
    	return HttpResponse(template.render(context))


#def log_view(request):
#	state="Please Login Below ........."   	
#	c={}
#	c.update(csrf(request))
#	logout(request)
#	username=password=''
#	if request.POST:
#  		username=request.POST.get('username')
#  	    	password=request.POST.get('password')
#	      	user=authenticate(username=username, password=password)
#	       	if user is not None:
#	        	if user.is_active:
#		  	     login(request, user)
#		 	     return HttpResponseRedirect('index')
#   			     state="You Are successfully logged in !!!"
#
#			else:	
#				state="Your Account is not active Please Contact the site admin"
#		else:
#			state="asdfasd"
#	template=loader.get_template('app/login.html')
#	context=RequestContext(request,{
#			'state':state,
#		'username':username,
#		}
#		)
#	return HttpResponse(template.render(context))
#	return HttpResponse(template.render(context),context_instance=RequestContext(request))
#	return render_to_response('login.html',{'state':state,'username':username},RequestContext(request))
@login_required
def dress(request):
#for i in image:
#	       	i.save()
#f=i;
#setattr(f,'image_urls',i.image_urls.encode())
#	setattr(f,'title',i.title.encode())
#	f.save()
#if not request.user.is_authenticated():
#	    return HttpResponseRedirect('/dress/login')
#	else:
#	    	user=request.user
    	cat=0
    	im=[0,1,2]
    	k=0
	ln=[]
	image=Person.objects.all()
	paginator=Paginator(image,12)
    	page=request.GET.get('page')
	try:
		images=paginator.page(page)
    	except PageNotAnInteger:
		images=paginator.page(1)
    	except EmptyPage:
		images=paginator.page(paginator.num_pages)
	for i in range(images.start_index(),images.end_index()+1):
	    ln.append(int(i)-1)
	lst=[]
	for i in range(1,paginator.num_pages):
	    lst.append(int(i))
	template=loader.get_template('apple3/dress.html')
	context=RequestContext(request,{
				   	    'image':image,
					    'k':k,
					    'im':im,
					    'ln':ln,
					    'images':images,
					    'lst':lst,
					    'paginator':paginator,
					    'cat':cat,
#'user':user,	    
					    }
				)
	return HttpResponse(template.render(context))
#    return HttpResponse(image)
@login_required
def title(request,title_id):
    	cur=0
	cur=Person.objects.get(pk=title_id)
#	imge=Person.objects.all()[:109]
#	for i in range(1,len(imge)-2):
#	    if i==int(title_id):
#	    	cur=imge[i]
	sz=str(cur.size)
	sz=sz.split(',')
	fsz=[]
	for i in sz:
	   s=""
	   for j in range(0,len(i)):
	    if i[j]!='U' and i[j]!='K' and i[j]!=',':
	    	s+=i[j]
	   fsz.append(s)
	lsz=len(fsz)
    	if request.method == 'POST':# If the form has been submitted...
        	form=UserForm(request.POST)# A form bound to the POST data
        	if form.is_valid(): # All validation rules pass
			form.cleaned_data
#form.userid=request.user
			new=form.save(commit=False)
    			new.userid=request.user
			new.save()
    			form.save_m2m()
			return HttpResponseRedirect('/')
    	else:
        	form = UserForm() # An unbound form"""
    	template=loader.get_template('apple3/title.html')
	context=RequestContext(request,{
			'cur':cur,
			'sz':fsz,
			'lsz':lsz,
			'form':form,
		}
		)
    	return HttpResponse(template.render(context))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required    
def male(request):
    	fl=0
    	image=Person.objects.filter(Q(category="male")|Q(category="Male"))
	if(len(image))==0:
	    fl=1
    	cat=1
	im=[0,1,2]
    	k=1
	ln=[]
#image=Person.objects.all()[:109]
	paginator=Paginator(image,12)
    	page=request.GET.get('page')
	try:
		images=paginator.page(page)
    	except PageNotAnInteger:
		images=paginator.page(1)
    	except EmptyPage:
		images=paginator.page(paginator.num_pages)
	for i in range(images.start_index(),images.end_index()+1):
	    ln.append(int(i)-1)
	lst=[]
	for i in range(1,paginator.num_pages):
	    lst.append(int(i))
	template=loader.get_template('apple3/dress.html')
	context=RequestContext(request,{
				   	    'image':image,
					    'k':k,
					    'im':im,
					    'ln':ln,
					    'images':images,
					    'lst':lst,
					    'paginator':paginator,
					    'cat':cat,
					    'fl':fl,
#'user':user,	    
					    }
				)
	return HttpResponse(template.render(context))
@login_required
def female(request):
    	cat=2
	fl=0
    	image=Person.objects.filter(Q(category="female")|Q(category="Female"))[:100]
	if(len(image)==0):
	    	fl=1
    	im=[0,1,2]
    	k=1
	ln=[]
#image=Person.objects.all()[:109]
	paginator=Paginator(image,12)
    	page=request.GET.get('page')
	try:
		images=paginator.page(page)
    	except PageNotAnInteger:
		images=paginator.page(1)
    	except EmptyPage:
		images=paginator.page(paginator.num_pages)
	for i in range(images.start_index(),images.end_index()+1):
	    ln.append(int(i)-1)
	lst=[]
	for i in range(1,paginator.num_pages):
	    lst.append(int(i))
	template=loader.get_template('apple3/dress.html')
	context=RequestContext(request,{
				   	    'image':image,
					    'k':k,
					    'im':im,
					    'ln':ln,
					    'images':images,
					    'lst':lst,
					    'paginator':paginator,
		    			    'cat':cat,
					    'fl':fl,
					    }
				)
	return HttpResponse(template.render(context))
def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form=ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
	    instance=form.save(commit=False)
    	    instance.save()
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    template=loader.get_template('apple3/new.html')
    context=RequestContext(request,{
			'form':form,	
		})
    return HttpResponse(template.render(context))
