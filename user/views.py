from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def login(request):
    return render(request, 'login.html')


def signup(request):
    #if request.method == 'POST':
    f_name = request.POST['full_name']
    email = request.POST['email']
    pass_1 = request.POST['password1']
    pass_2 = request.POST['password2']
    address = request.POST['address']
    user = User.objects.create_user(
	        username=email,
		    email=email,
		    password=pass_1,
		    first_name = f_name,
		    last_name = l_name,
		)
    return render(request, 'signup.html')
