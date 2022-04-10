from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import bookdata
from .models import User
from django.contrib import messages
import mysql.connector as sql

# Create your views here.
def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method == "POST":
        my = sql.connect(host="localhost",user="root",password="root",database="LMS")
        cursor = my.cursor()
        d = request.POST
        for Key,Value in d.items():
            if Key =="email":
                em = Value
            if Key =="password":
                pwd = Value       
        c = "select * from reg where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t==():
            return render(request,'index.html')
        else:
            return render(request,'book.html')

    return render(request,'signin.html')

def adminlogin(request):
    if request.method == "POST":
        my = sql.connect(host="localhost",user="root",password="root",database="LMS")
        cursor = my.cursor()
        data = request.POST
        for Key,Value in data.items():
            if Key =="ufirst":
                fs = Value
            if Key =="upass":
                ps = Value
        c1 = "select * from admin1 where ufirst ='{}' and upass='{}'".format(fs,ps)
        cursor.execute(c1)
        t1 = tuple(cursor.fetchall())
        if t1==():
            return render(request, 'index.html')
        else:
            return redirect('add')

    return render(request,'adminlogin.html')
    
def signup(request):
    if request.method == "POST":
        my = sql.connect(host="localhost",user="root",password="root",database="LMS")
        cursor = my.cursor()
        d = request.POST
        for Key,Value in d.items():
            if Key =="firstname":
                fn = Value
            if Key =="lastname":
                ls = Value
            if Key =="email":
                em = Value
            if Key =="password":
                pwd = Value
            if Key =="phone":
                ph = Value
                messages.success(request, 'Registerd successfully..Now ready to signin !! ')

        c = "insert into reg Values('{}','{}','{}','{}','{}')".format(fn,ls,em,pwd,ph)
        cursor.execute(c)
        my.commit()
    return render(request,'signup.html')


def adminreg(request):
    if request.method == "POST":
        my = sql.connect(host="localhost",user="root",password="root",database="LMS")
        cursor = my.cursor()
        data = request.POST
        for Key,Value in data.items():
            if Key =="ufirst":
                fs = Value
            if Key =="ulast":
                lt = Value
            if Key =="uname":
                nm = Value
            if Key =="upass":
                ps = Value
            if Key =="uphone":
               cont = Value
               messages.success(request, 'Registerd successfully..Now ready to signin !! ')

        c1 = "insert into admin1 Values('{}','{}','{}','{}','{}')".format(fs,lt,nm,ps,cont)
        cursor.execute(c1)
        my.commit()

    return render(request,'adminreg.html')

def add(request):
    if request.method == 'POST':
        fm = bookdata(request.POST)
        if fm.is_valid():
            messages.success(request, 'Data successfully added !!')
            fm.save()
            fm = bookdata()
    else:
        fm = bookdata()
    data = User.objects.all()
    return render(request,'add.html',{'form':fm ,
    'stu':data})
    
def delete_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add')

def updatedata(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm = bookdata(request.POST,instance = pi)
        if fm.is_valid():
            messages.success(request, 'Data successfully updated !!')
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = bookdata(instance = pi)
    return render(request, 'update.html',{'form':fm})

def book(request):
    return render(request,'book.html')

def Logout(request):
    logout(request)
    messages.success(request,'logout')
    return redirect('index')
   