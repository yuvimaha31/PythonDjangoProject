"""
URL configuration for projectname project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from bro_app import views

from bro_app.views import OrderReg, Orderlist ,Orderdetail , OrderUpdate, OrderDelete 

app_name='bro_app'

urlpatterns = [
    path('home', views.home, name = "home"),
    path('product', views.product, name = "product"),
    path('service', views.service, name = "service"),
    path('contact', views.contact, name = "contact"),
    path('aboutus', views.aboutus, name = "aboutus"),
    

   path('Orderreg', OrderReg.as_view(), name = 'Orderreg'),
   path('<pk>/Orderdetail', Orderdetail.as_view(), name = 'Orderdetail'),
   path('',Orderlist.as_view(), name = 'Orderlist'),
   path('<pk>/Orderupdate',OrderUpdate.as_view(),name = 'Orderupdate'),
   path('<pk>/Orderdelete', OrderDelete.as_view(), name = 'Orderdelete'),


### for get ad post
    path('dhana',views.dhana, name = 'dhana'),
    path('get1', views.get1, name = 'get1'),
    path('post1', views.post1, name = 'post1'),

###  for Fnuction based view.
    path('form', views.form,name  = 'form'), ##Order registration
    path('Orders', views.Order, name = "Orders"), #Orderlist
    path('detail/<int:id>', views.detail, name = 'detail'), # Order Detail
    path('update/<int:id>', views.update, name = 'update'), # Stuudent update
    path('delete/<int:id>', views.delete, name = 'delete'), #Order Update

### for user registratio, sign-in sign-out
    path('index', views.index, name = 'index'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

    
    path('', views.home, name='home'),
    path("image",views.image, name='image'),
    path('images', views.images, name='images'),
    
    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart '),
   
    
]


