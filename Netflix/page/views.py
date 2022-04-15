from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def index_user_2(request):
    return render(request, 'index-user-2.html')

def index_user_3(request):
    return render(request, 'index-user-3.html')


def login(request):
    return render(request, 'login.html')

def users(request):
    return render(request, 'usuarios.html')