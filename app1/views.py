from django.shortcuts import render,redirect

app_name="app1"


def index(request):
    return render(request,'app1/base.html')
