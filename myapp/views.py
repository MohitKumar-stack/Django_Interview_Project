from django.shortcuts import render,redirect
from .models import databse
# Create your views here.


def index(request):
    if request.method =='POST':
        Email =request.POST.get("Email")
        password =request.POST.get("password")
        if databse.objects.filter(Email=Email,Password=password).exists():
            return redirect('/home')
    return render(request,'login.html')



def Signup(request):
    if request.method =='POST':
        username =request.POST.get("username")
        email =request.POST.get("mail")
        password =request.POST.get("password")
        Cpassword =request.POST.get("Cpassword")
        address =request.POST.get("address")
        username =request.POST.get("username")
        Data= databse(Email=email,UserName=username,Address=address,Password=password)
        Data.save()
        return redirect('/home')
    return render(request,'Signup.html')




def Home(request):
    data=databse.objects.all()
    user={
        'user_data':data
    }
    return render(request,'Home.html',user)





def delete(request,id):
    data=databse.objects.filter(id=id)
    data.delete()
    return redirect('/home')




def update(request,id):
    username =request.POST.get("username")
    email =request.POST.get("mail")
    address =request.POST.get("address")
    databse.objects.filter(id=id).update(Email=email,UserName=username,Address=address)
    return redirect('/home')




def edit(request,id):
    data=databse.objects.filter(id=id)
    user={
        'user_data':data
    }
    return render(request,'update.html',user)