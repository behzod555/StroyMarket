from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import json
import datetime
from .models import * 
from .forms import *
from .utils import cookieCart, cartData, guestOrder
from django.db.models import Q

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories = Category.objects.filter(parent=None)
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	products = Product.objects.all()
	novinki = Product.objects.filter(novinki=True)
	popularnye = Product.objects.filter(popularnye=True)
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0

	context = {'novinki':novinki,'popularnye':popularnye,'products':products, 'cartItems':cartItems, 'order':order, 'items':items, 'categories':categories,'wishedProducts':wishedProducts,'count':count,'wishedProductsList':wishedProductsList,'categories_for_menu':categories_for_menu}
	return render(request, 'store/store.html', context)

def ProductItems(request):
	products = Product.objects.all()
	context = {
	'products':products,
	}
	return render(request,'store/product-items.html', context)
def WishlistItems(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	categories = Category.objects.filter(parent=None)
	products = Product.objects.all()
	user = request.user
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0
	


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items, 'categories':categories,'wishedProducts':wishedProducts,'count':count,'wishedProductsList':wishedProductsList,'categories_for_menu':categories_for_menu}
	return render(request, 'store/wishlist.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	categories = Category.objects.all()
	products = Product.objects.all()
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0

	context = {'products':products,'items' : items, 'order' : order, 'cartItems' : cartItems,'wishedProducts':wishedProducts,'count':count,'wishedProductsList':wishedProductsList,'categories_for_menu':categories_for_menu}
	return render(request, 'store/cart.html', context)
@login_required(login_url="{% url 'login' %}")
def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	
	"""if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)
	if request.method == 'POST':
		order.imya = request.POST.get('name')
		order.familiya = request.POST.get('surname')
		order.email = request.POST.get('email')
		order.tel = request.POST.get('number')
		order.adres = request.POST.get('address')
		order.city = request.POST.get('city')
		order.state = request.POST.get('state')
		order.save()
		if order.save():
			return redirect(request,'store')"""
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	categories = Category.objects.all()
	products = Product.objects.all()
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0

	context = {'products':products,'items' : items, 'order' : order, 'cartItems' : cartItems,'wishedProducts':wishedProducts,'count':count,'wishedProductsList':wishedProductsList,'categories_for_menu':categories_for_menu}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	quantity = data['quantity']
	print('Action:', action)
	print('Product:', productId)
	print('Quantity:',quantity)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + quantity)

	if action == 'remove':
		orderItem.quantity = (orderItem.quantity - quantity)

	orderItem.save()
	
	if action=='delete':
		orderItem.quantity=0

	if orderItem.quantity <= 0:
		orderItem.delete()

	
	return JsonResponse('Item was added', safe=False)

def addWishlistView(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)
	user = request.user
	product = Product.objects.get(id=productId)
	deleted = Wishlist.objects.filter(user=user, product=product).delete()
	if deleted == (0, {}):
		Wishlist.objects.get_or_create(user=user, product=product)
		print("True")
	


	return JsonResponse('Item was added', safe=False)

def product_details(request,category_slug, slug):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories = Category.objects.filter(parent=None)
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	product = get_object_or_404(Product, slug=slug)
	products = Product.objects.all()
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0
	context = {'items' : items, 'order' : order, 'cartItems' : cartItems, 'product':product,'products':products, 'categories':categories,'categories_for_menu':categories_for_menu,'wishedProducts':wishedProducts,'wishedProductsList':wishedProductsList,'count':count}
	return render(request, "store/product-details.html", context)

def category_detail(request, slug):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	categories = Category.objects.filter(parent=None)
	category = get_object_or_404(Category, slug=slug)
	products_all = Product.objects.filter(Q(category = category)|Q(category__parent = category))
	print(products_all)
	products = category.products.all()
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0
	context = {'items' : items, 'order' : order, 'cartItems' : cartItems, 'products':products, 'category':category, 'categories':categories,'categories_for_menu':categories_for_menu,'products_all':products_all,'wishedProducts':wishedProducts,'wishedProductsList':wishedProductsList,'count':count}
	
	return render(request, "store/categories.html", context)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	name = data['form']['name']
	email = data['form']['email']
	phone = data['form']['number']
	phoneAdd = data['form']['numberAdd']
	address = data['form']['address']
	time = data['form']['time']
	date = data['form']['date']
	payment = data['form']['payment']
	comment = data['form']['comment']
	id_order = int(data['form']['id'])



	if request.user.is_authenticated:
		customer = request.user.customer
		order = Order.objects.get(id=id_order)
		order.transaction_id = transaction_id 
		order.complete=True
		order.save()
		
		OrderInfo.objects.create(customer=customer,order=order,name=name,email=email,phone=phone,phoneAdd=phoneAdd,address=address,time=time,date=date,payment=payment,comment=comment)


	else:
		print("Not logged in ")
	
	return JsonResponse('Payment submitted..', safe=False)
def Search(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	categories = Category.objects.filter(parent=None)
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0


	if request.method == "POST":
		query_name = request.POST.get('search', None)
		
		if query_name:
			results = Product.objects.filter(name__contains=query_name)
			return render(request, 'store/search.html', {'items' : items, 'order' : order, 'cartItems' : cartItems,"results":results,"query_name":query_name,'categories_for_menu':categories_for_menu,'wishedProducts':wishedProducts,'wishedProductsList':wishedProductsList,'count':count})


	return render(request, 'store/search.html', {'items' : items, 'order' : order, 'cartItems' : cartItems, 'categories':categories,'categories_for_menu':categories_for_menu,'wishedProducts':wishedProducts,'wishedProductsList':wishedProductsList,'count':count})
	

def calculator(request):
	data = cartData(request)
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	categories = Category.objects.filter(parent=None)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0


	context = {'items' : items, 'order' : order, 'cartItems' : cartItems, 'categories':categories,'categories_for_menu':categories_for_menu,'wishedProducts':wishedProducts,'wishedProductsList':wishedProductsList,'count':count}
	return render(request,"store/calculator.html", context)

def Privacy(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	categories_for_menu = Category.objects.filter(parent=None)[:6]
	categories = Category.objects.filter(parent=None)

	if request.user.is_authenticated:
		user=request.user
		wishedProducts = Wishlist.objects.filter(user=user)
		wishedProductsList = []
		for i in wishedProducts:
			wishedProductsList.append(i.product)
		count = Wishlist.objects.filter(user=user).count()
		if count>0:
			count=True
		else:
			count=False
	else:
		wishedProducts = {}
		wishedProductsList={}
		count=0
		
	context = {'items' : items, 'order' : order, 'cartItems' : cartItems, 'categories':categories,'categories_for_menu':categories_for_menu,'wishedProducts':wishedProducts,'wishedProductsList':wishedProductsList,'count':count}
	return render(request,"store/privacy.html",context)