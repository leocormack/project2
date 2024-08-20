from django.shortcuts import render, redirect


# Create your views here.

def home(request):

	context = {
		'home_active': 'active',
	}
		
	return render(request, 'index.html', context)

def test(request):

	context = {
		'test_active': 'active',
	}
		
	return render(request, 'test.html', context)
