from django.shortcuts import render,redirect
from app1.models import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         roll=request.POST.get('roll')
#         summary=request.POST.get('summary')
#         inst=Contact() 
#         inst.name=name
#         inst.roll=roll
#         inst.summary=summary
#         inst.save()
#     return render(request,'app1/index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        summary=request.POST.get('summary')
        inst=Contact(name=name,roll=roll,summary=summary) 
        inst.save()
    return render(request,'app1/index.html')




def fun(request):
    return redirect('/send/')



#send data in frontend
def sendData(request):
    info=Contact.objects.all()
    # serializer=ContactSerializer(info)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    context = {"data":info}
    return render(request,'app1/contact.html', context)

#send data in frontend
def Edit(request,id):
    info=Contact.objects.get(id=id)
    context = {"data":info}
    if request.method=="POST":
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        summary=request.POST.get('summary')
        info.name=name
        info.roll=roll
        info.summary=summary
        info.save()
        return redirect('/send/')
    return render(request,'app1/edit.html',context)




def Delete(request,id):
    info=Contact.objects.get(id=id)
    info.delete()
    return redirect('/send/')



def createmethod(request):
    if request.method=="POST":
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        summary=request.POST.get('summary')
        inst=Contact()
        inst.name=name
        inst.roll=roll
        inst.summary=summary
        inst.save()
        return redirect('/send/')
    return render(request,'app1/home.html')



def updatemethod(request,pk):
    info=Contact.objects.get(id=pk)
    print('@@@@@@@@@@@@@@@@@@@@@@@222')
    if request.method=="POST":
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        summary=request.POST.get('summary')
        info.name=name
        info.roll=roll
        info.summary=summary
        info.save()
        context={'data':info}
        print('@@@@@@@@@@@@@@@@@@@@@@@222')
        return redirect('/send/')
    return render(request,'app1/edit.html',context)
    # return render(request,'app1/edit.html', context)
    