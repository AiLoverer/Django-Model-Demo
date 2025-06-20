from django.shortcuts import render
from modelapp.models import Person
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from modelapp.models import Person
from datetime import datetime

# Create your views here.

def index(request):
    persons = Person.objects.all()
    #return HttpResponse("Hello, world. You're at the modelapp index.")
    #return render(request, 'index.html', {'persons': persons})
    return HttpResponse('<h1>首页</h1><a href="/users">用户信息管理</a>')

def person_list(request):
    try:
        persons = Person.objects.all()
        return render(request, 'modelapp/person/index.html', {'persons': persons})
    except Person.DoesNotExist:
        persons = None
        return HttpResponse('<h1>没有任何用户信息</h1><a href="/users/person_add">创建用户信息</a>')
    

def person_add(request):
    return render(request, 'modelapp/person/add.html')

def person_insert(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            print(name)
            age = request.POST['age']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            person = Person(name=name, age=age, email=email, phone=phone, address=address)
            person.save()
            context = {'info': '添加成功'}
            print(context)
            print(person)
        except:
            context = {'info': '添加失败'}
            print(context)
        return render(request, 'modelapp/person/info.html', context)
def person_edit(request, pk):
    try:
        person = Person.objects.get(id=pk)
        context = {'person': person}
        return render(request, 'modelapp/person/edit.html', context)
    except :
        context = {'info': '没有该用户信息'}
        return render(request, 'modelapp/person/info.html', context)

def person_update(request):
    print('person_update')
    try:
        person = Person.objects.get(id = request.POST['id'])
        person.name = request.POST['name']
        person.age = request.POST['age']
        person.email = request.POST['email']
        person.phone = request.POST['phone']    
        person.address = request.POST['address']
        person.updated_at = datetime.now()
        person.save()
        context = {'info': '更新成功'}
        return render(request, 'modelapp/person/info.html', context)
    except:
        context = {'info': '更新失败'}
        return render(request, 'modelapp/person/info.html', context)

def person_delete(request, pk):
    try:
        person = Person.objects.get(id=pk)
        person.delete()
        context = {'info': '删除成功'}
    except: 
        context
    return render(request, 'modelapp/person/info.html', context)
    