from django.shortcuts import render

def index(request):
    return render(request,'index.html',{})

def simple(request):
    return render(request,'simple.html',{})
def dinamico(request,name):
    categories = {'code','design','marketing','bussings'}
    context= {'name' : name, 'categories':categories} 
    return render(request,'dinamico.html',context)

def estaticos(request):
    return render(request, 'estaticos.html',{})
def herencia(request):
    return render(request,'herencia.html',{})
