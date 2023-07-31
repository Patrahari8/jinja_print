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

def nested_if(request):
    d={'a':100,'b':20,'c':50}
    return render(request,'nested_if.html',context=d)

def jinja_for(request):
    d={'name':'hari','hobbies':['badminton','drawing']}
    return render(request,'jinja_for.html',context=d)