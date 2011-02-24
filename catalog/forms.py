from django import forms
from project1.catalog.models import  Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        
    def clean_price(self):
        if self.cleaned_data['price'] <= 0 :
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']

class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.TextInput( attrs ={
              'size':2,'value':1,'class':'quantity','maxlength':5
            }))        
    product_slug = forms.CharField(widget=forms.HiddenInput())
    
    def __init__(self,request=None,*args,**kwargs):
        self.request = request
        super(ProductAddToCartForm,self).__init__(*args,**kwargs)
    
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookie must be enabled")
        
        return self.cleaned_data
    
                
    