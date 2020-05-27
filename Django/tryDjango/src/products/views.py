from django.shortcuts import render

from .forms import ProductForm, RawProductForm

from .models import Product


# def product_create_view(request):
# 	my_form = RawProductForm()
# 	if(request.method == "POST"):
# 		my_form = RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			#The data is proper
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.error)
# 	context = {
# 		"form" : my_form
# 	}
# 	return render(request,"products/product_create.html",context)

# def product_create_view(request):
# 	# print(request.GET)
# 	if request.method == "POST":
# 		my_new_title = request.POST.get('title');
# 		print(my_new_title)
# 		# Product.objects.create(title=my_new_title)      ---> to create a new object in db
# 	context = {}
# 	return render(request,"products/product_create.html",context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()

	context = {
	 	'form' : form
	}
	return render(request,"products/product_create.html",context)

# Create your views here.
def product_detail_view(request):
	obj = Product.objects.get(id=1)
	# context = {
	# 'title' : obj.title,
	# 'description' : obj.description
	# }

	context = {
	 	'object' : obj
	}
	return render(request,"products/product_detail.html",context)

def dynamic_lookup_view(request,id):
	obj =Product.objects.get(id=id)
	context = {
		'object' : obj
	}

	return render(request,"products/product_detail.html",context)