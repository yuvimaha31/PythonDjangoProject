from django.shortcuts import render

# Create your views here.
	
#Class based views
from charan.models import Order

from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView

class OrderReg(CreateView):
	model =Order
	fields = '__all__'
	template_name = 'Dhana/Orderreg.html'
	success_url ="/"

class Orderlist(ListView):
	model =Order
	template_name = 'Dhana/Orderlist.html'

class Orderdetail(DetailView):
	model =Order
	template_name = 'Dhana/Orderdetail.html'

class OrderUpdate(UpdateView):
	model =Order
	fields = "__all__"
	template_name = 'Dhana/Orderupdate.html'
	success_url ="/"


class OrderDelete(DeleteView):
	model =Order
	template_name = 'Dhana/Orderdelete.html'
	success_url ="/"
