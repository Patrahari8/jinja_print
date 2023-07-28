from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'hari','pro':'python developer','age':22}
    return render(request,'data_render.html',context=d)

def if_else(request):
    d={'a':100,'b':20}
    return render(request,'if_else.html',context=d)
def if_elif(request):
    d={'a':100,'b':2000,'c':500000}
    return render(request,'if_elif.html',context=d)