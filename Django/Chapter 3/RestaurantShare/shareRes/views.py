from django import http
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/index.html', content)

def restaurantDetail(request):
    return render(request, "shareRes/restaurantDetail.html")

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, "shareRes/restaurantCreate.html", content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id=category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category=category, restaurant_name=name, restaurant_link=link,
                        restaurant_content=content, restaurant_keyword=keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, "shareRes/categoryCreate.html", content)

def Create_category(request):
    category_name = request.POST['categoryName'] # html input 태그의 name
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request):
    category_id = request.POST['categoryID']
    delete_category = Category.objects.get(id=category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))
