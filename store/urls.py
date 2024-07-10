from django.urls import path

from store.views import *
from auth import views
urlpatterns = [
	#Leave as empty string for base url
	path('', store, name="store"),
	path('cart/', cart, name="cart"),
	path('checkout/', checkout, name="checkout"),
	path('calculator/', calculator, name="calculator"),
	path('policy/',Privacy,name="privacy"),
	path('wishlist/', WishlistItems, name="wishlist"),
	path('update_item/', updateItem, name="update_item"),
	path('add_wishlist/', addWishlistView, name="add_wishlist"),
	path('login/', views.LoginForm, name="login"),
	path('product-items/', ProductItems, name="product-items"),
	path('otp/', views.send_otp, name="otp"),
	path('search/', Search, name="search"),
	path('register/',views.Register,name="register"),
	path('logout/',views.logoutUser,name="logout"),
	path('process_order/', processOrder, name="process_order"),
	path('<slug:category_slug>/<slug:slug>/', product_details, name="product_details"),
	path('<slug:slug>/', category_detail, name="category_detail"),
	
]
