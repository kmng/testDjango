# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from project1.catalog.models import  Category, Product
from django.template import RequestContext

def index(request,template_name = 'catalog/index.html'):
    page_title = 'Musical Instuments and Sheet Music for Musicians'
    return render_to_response(template_name,locals(),
            context_instance = RequestContext(request))