from project1.catalog.models import Category
from project1 import settings

def project1(request):
    return {
            'active_categories': Category.objects.filter(is_active=True),
            'site_name' : settings.SITE_NAME,
            'meta_keywords' : settings.META_KEYWORDS,
            'meta_description' : settings.META_DESCRIPTION,
            'request' : request ,             
            
            }