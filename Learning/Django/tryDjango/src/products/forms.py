from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Title"}))
	description = forms.CharField(required=False,widget=forms.Textarea(attrs={"class":"my_class_name my_second_class",
								  		"placeholder":"Description",
								  		"id":"my_id",
								  		"rows":15,
								  		"columns":15
								  		}))
	price 		= forms.DecimalField(initial=199.99)
	class Meta:
		model = Product
		fields = [
		'title',
		'description',
		'price'
		]

	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get('title');
		if 'CFE' in title:
			return title
		else:
			raise forms.ValidationError("This is not a valid title")

class RawProductForm(forms.Form):
	title 		= forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"Title"}))
	description = forms.CharField(	required=False,
								  	widget=forms.Textarea(
								  		attrs={
								  		"class":"my_class_name my_second_class",
								  		"placeholder":"Description",
								  		"id":"my_id",
								  		"rows":15,
								  		"columns":15
								  		}))
	price 		= forms.DecimalField(initial=199.99)