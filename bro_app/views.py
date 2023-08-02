
## for user creation or register, sign-in and sign-out.
from django.shortcuts import render, redirect,get_object_or_404

from bro_app.forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 
 

def register(request):	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('bro_app:login_reg')


	context = { 'form': form }
	return render (request, 'signin/register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('bro_app:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'signin/login.html', context)

def logoutuser(request):
	logout(request)
	# return redirect('bro_app:login_reg')
	return redirect('bro_app:home')


@login_required(login_url = 'bro_app:login_reg')
def index(request):
	return render (request,"signin/index.html", context = {})


from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def product(request):
    return render(request, 'product.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def aboutus(request):
    return render(request, 'aboutus.html')



from bro_app.models import Order

# defOrders(request):
#    Order =Order.objects.all()
#     context = {'student':student}
#     return render(request, 'student.html', context)

	
#Class based views


from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class OrderReg(CreateView):
	model =Order
	fields = '__all__'
	template_name = 'CBV/Orderreg.html'
	success_url ="/"

class Orderlist(ListView):
	model =Order
	template_name = 'CBV/Orderlist.html'

class Orderdetail(DetailView):
	model =Order
	template_name = 'CBV/Orderdetail.html'

class OrderUpdate(UpdateView):
	model =Order
	fields = "__all__"
	template_name = 'CBV/Orderupdate.html'
	success_url ="/"


class OrderDelete(DeleteView):
	model =Order
	template_name = 'CBV/Orderdelete.html'
	success_url ="/"



# for get and post

def dhana(request):
	return render(request,'formmet/dhana.html')

def get1(request):
	a = int(request.GET['num1'])
	b = int(request.GET['num2'])
	c = a*b
	context = {'c': c }
	return render(request,'formmet/get.html',context)

def post1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a*b
	context = {'c': c }
	return render(request,'formmet/post.html',context)

	#### For Function based view

from django.shortcuts import render , redirect, get_object_or_404

from .models import Order
from .forms import OrderForm

### for Orderlistview
def Orders(request):
    Order = Order.objects.all()
    context = {'Order':Order}
    return render(request, 'Order.html', context)


def detail(request, id):
	data = Order.objects.get(id = id)	
	context = {'data':data}
	return render(request,'FBV/detail.html', context)


def update(request, id):
	obj = get_object_or_404(Order, id =id)
	form = OrderForm(request.POST or None, instance = obj)
	data = Order.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('bro_app:Orders')

	context = {'form':form, 'data':data}
	return render(request,'FBV/update.html', context )


def delete(request, id):
	data = Order.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('bro_app:form')
	return render(request,'FBV/delete.html', context )


def form(request):
    stu = Order.objects.all() 

    form = OrderForm
    if request.method =="POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bro_app:Orders')  

    context = {'Ord': Ord, 'form': form}
    return render(request, 'FBV/form.html', context) 

from django.shortcuts import render
from .forms import ImageForm
from .models import Image


def image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp/image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'imageapp/image.html', {'form': form})

def images(request):
    all_images=Image.objects.all()
    context={'all_images':all_images}
    return render(request, 'imageapp/images.html', context)


from .forms import ProductForm, OrderXForm
from .models import Product


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'imageapp/product.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'imageapp/product.html', {'form': form})

def products(request):
    all_products=Product.objects.all()
    context={'all_products':all_products}
    return render(request, 'imageapp/products.html', context)

def order(request, id):
    obj = get_object_or_404(Product, id =id)
    form = OrderXForm(request.POST or None, instance = obj)
    data = Product.objects.get(id = id)
    if form.is_valid():
        form.save()
        return redirect('products')
    context = {'form':form, 'data':data}
    return render(request, 'imageapp/order.html', context)

def kart(request):
    Ordered_items = Product.objects.filter(order_status = True)
    print("Ordered Items :", Ordered_items)
    price = Product.objects.values('price')[0]
    total = 0
    total_value = 0
    for price in Ordered_items:
        print(price.price)
        print(price.items)
        total = price.price*price.items
        total_value = total_value+total
        print(total)

    print(total_value)
    context = {'Ordered_items':Ordered_items, 'total':total_value}
    return render(request, 'imageapp/kart.html', context)