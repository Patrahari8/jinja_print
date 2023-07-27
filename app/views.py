from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'hari','pro':'python developer','age':5}
    return render(request,'data_render.html',context=d)