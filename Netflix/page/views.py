from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'homepage.html')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def index_user_2(request):
    return render(request, 'index-user-2.html')

@login_required
def index_user_3(request):
    return render(request, 'index-user-3.html')

@login_required
def login(request):
    return render(request, 'login.html')

@login_required
def users(request):
    return render(request, 'usuarios.html')