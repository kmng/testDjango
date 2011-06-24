# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def register(request, template_name="registration/register.html"):
    if request.method == 'POST':
        postdata =request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            from django.contrib.auth import login,authenticate
            new_user = authenticate(username=un,password=pw)
            if new_user and new_user.is_active:
                login(request,new_user)
                url = urlresolver.reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = UserCreationForm()
    page_title = 'User Registration'
    return render_to_response(template_name,locals(),context_instance = RequestContext(request))

def my_account(request,template_name="registration/my_account.html"):
    page_title ='My Account'
    name = request.user.username
    
    return render_to_response(template_name,locals(),context_instance = RequestContext(request))
