from django.shortcuts import render,redirect
from .forms import CreateUserForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from store.models import *
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

from twilio.rest import Client

import random,os
# Create your views here.
def Register(request):
	form = CreateUserForm()
	phonenumber = request.POST.get('phone')
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			Profile.objects.create(user=user,phonenumber=phonenumber)
			generate_otp(phonenumber)
			return redirect('otp')

	

	

	context = {
	'form':form,
	
	}
	return render(request, 'store/register.html', context)


def LoginForm(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password = password)
		if user is not None:
			login(request, user)
			user = request.user
			profile = Profile.objects.get(user=user)
			if profile.verified == True:
				if Customer.objects.filter(user=user).exists():
					print("Exists:")
				else:
					Customer.objects.create(user=user,name=user)
				return redirect('store')
			else: 
				return redirect('register')

	context = {}
	
	return render(request, 'store/login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('login')

def generate_otp(mobile_no):

	otp=random.randint(1000,9999)
	account_sid = 'AC4c938c2a2203b2de569f12483a4334ea'
	auth_token = '726a7db16fc56f04b84a66f4ac9215b4'
	client = Client(account_sid, auth_token)
	client.messages.create(
		to=mobile_no,
		from_="+15805308602",
		body='Your One Time Password is '+str(otp))

	#print otp
	f=open('/home/b/baihouse20/public_html/StroyMarket/otp.txt','w')
	f.write(str(mobile_no))
	f.write(str(otp))
	f.close()


def send_otp(request):
	otp=0

	if request.method == 'POST':
		otp = request.POST.get('otp')
		f=open('/home/b/baihouse20/public_html/StroyMarket/otp.txt','r')
		file=f.read()
		phonenumber=file[0:13]
		otp_read = file[13:17]
		f.close()
		open('/home/b/baihouse20/public_html/StroyMarket/otp.txt','w').close()
		print(otp)
		print(phonenumber)
		print(otp_read)
		#print otp,entered_otp
		if int(otp_read)==int(otp):
			profile=Profile.objects.get(phonenumber=phonenumber)
			print(profile)
			profile.verified = True
			profile.save()
			return redirect('login')
		else:
			return HttpResponseRedirect(reverse('Failure'))
	

	
	return render(request,'store/otp.html',{})