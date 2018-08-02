from django.shortcuts import render

def index(request):
	return render(request, 'mainApp/homePage.html')

def contact(request):
	return render(request, 'contact/contact.html')

def sing_in(request):
	return render(request, 'sing_in/sing_in.html')