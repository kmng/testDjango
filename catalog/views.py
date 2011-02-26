# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from project1.catalog.models import  Category, Product
from django.template import RequestContext
from django.core import urlresolvers
from project1.cart import cart
from django.http import HttpResponseRedirect
from project1.cart.forms import ProductAddToCartForm


def index(request,template_name = 'catalog/index.html'):
    page_title = 'Musical Instuments and Sheet Music for Musicians'
    return render_to_response(template_name,locals(),
            context_instance = RequestContext(request))

def show_category(request,category_slug,template_name = 'catalog/category.html'):
    c = get_object_or_404(Category,slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name,locals(),
            context_instance = RequestContext(request))

def show_product(request,product_slug,template_name='catalog/product.html'):
    p = get_object_or_404(Product,slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    if request.method == 'POST':
        postdata = request.POST.copy()
        from = ProductAddToCartForm(postdata)
        if form.is_valid():
            cart.add_to_cart(request)
            if
    return render_to_response(template_name,locals(),
            context_instance = RequestContext(request))
     
