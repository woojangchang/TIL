# Chapter 3

## 1.2 SET URLs and Templates

챕터 2의 1.1~1.4를 반복

- 장고 프로젝트 생성
- secret key 숨기기
- 앱 2개 생성 (ShareRes, SendEmail)
- Templates 폴더 생성 후 html 파일 추가 (github)
- `RestaurantShare/urls.py`의 내용 수정

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('shareRes.urls')),
    path('sendEmail/', include('sendEmail.urls')),
    path('admin/', admin.site.urls),
]
```

- `RestaurantShare/shareRes/urls.py`, `RestaurantShare/sendEmail/urls.py` 생성

```python
# /sendEmail/urls.py
from django.urls import path, include
from . import views
urlpatterns = [
    path('send/', views.sendEmail)
]
```

```python
# /shareRes/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail),
    path('restaurantCreate/', views.restaurantCreate),
    path('categoryCreate/', views.categoryCreate),
]
```

- 각각의 `views.py`에 함수 생성

```python
# /shareRes/views.py
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shareRes/index.html')

def restaurantDetail(request):
    return render(request, "shareRes/restaurantDetail.html")

def restaurantCreate(request):
    return render(request, "shareRes/restaurantCreate.html")

def categoryCreate(request):
    return render(request, "shareRes/categoryCreate.html")
```

```python
# sendEmail/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sendEmail(request):
    return HttpResponse("sendEmail")
```

## 1.3 CRUD

### Category

#### Create

하나의 맛집이 하나의 카테고리에 속하는 방법 구현

1. 카테고리 데이터 베이스 생성

```python
# /models.py
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
```

- `python manage.py makemigrations`
- `python manage.py migrate`

2. `/categoryCreate/create/` url을 활성화
   - `categoryCreate.html`에서 추가 버튼을 누르면 `./create`로 연결되도록 되어있다.

```python
# /shareRes/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail, name='resDetailPage'),
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    path('categoryCreate/', views.categoryCreate, name='cateCreatePage'),
    
    # 추가한 코드
    path('categoryCreate/create', views.Create_category, name='cateCreate'),
]
```

3. 입력 받은 카테고리를 데이터 베이스에 저장

```python
# /models.py

# 추가한 코드
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def Create_category(request):
    category_name = request.POST['categoryName'] # html input 태그의 name
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
```

#### Read

1. 추가한 카테고리를 메인 페이지에 표시 (`index.html`)

```python
# /shareRes/views.py
# 수정한 코드
def index(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/index.html', content)
```

```html
<ul class="restaurantListDiv nav nav-pills nav-stacked">
    {% for category in categories %}
    <li class="category deactive">{{ category.category_name }}</li>
    <ul class="restaurantList">

        <div class="input-group">
            <span class="input-group-addon">
                <input name="check1" id="check1" type="checkbox">
            </span>
            <a href="restaurantDetail/1"><input name="res1" id="res1" type="text" class="form-control" disabled style="cursor: pointer;" value="1"></a>
        </div>

        <div class="input-group">
            <span class="input-group-addon">
                <input name="check2" id="check2" type="checkbox">
            </span>
            <a href="restaurantDetail/2"><input name="res2" id="res2" type="text" class="form-control" disabled style="cursor: pointer;" value="2"></a>
        </div>

    </ul>
    {% endfor %}
</ul>
```

2. 카테고리 추가하기 페이지에서도 카테고리 목록 표시 (`createCategory.html`)

```python
# /shareRes/views.py
# 수정한 코드
def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, "shareRes/categoryCreate.html", content)
```

```html
{% for category in categories %}
<form action="" method="POST">{% csrf_token %}
    <div class="input-group">
        <span class="input-group-addon" id="" style="border:1px solid #ccc; border-radius: 4px;">{{ category.category_name }}</span>
        <input type="hidden" name="categoryId" id="categoryId" value="{{ category.id }}"/>
        <input type="submit" class="resAddBtn btn btn-danger" role="button" value="삭제"/>
    </div>
</form>
{% endfor %}
```

- 기본 그룹 : 모든 식당은 하나의 카테고리에 무조건 속해야 하므로 필요한 그룹, 카테고리를 삭제했을 때 해당 카테고리에 있던 식당을 옮기기 위한 그룹

  - 기본 그룹을 데이터 베이스에 추가하기

    1. '카테고리 추가' 페이지에서 '기본 그룹'을 직접 추가
    2. cmd에서 `python manage.py dbshell` 입력
    3. `.tables`로 테이블 명 확인 후 `select * from shareRes_category;` 입력하여 id 확인 (나의 경우는 3)
    4. `.quit`로 빠져나옴
    5. html에서 '기본 그룹' 아래에 또 '기본 그룹'이 뜨지 않게 설정 (`categoryCreate.html`)

    ```html
    {% for category in categories %}
    {% if category.id == 3 %}
    <div class="input-group">
        <span class="input-group-addon" style="border:1px solid #ccc; border-radius: 4px;">{{ category.category_name }}</span>
    </div>
    {% endif %}
    {% endfor %}
    
    {% for category in categories %}
    {% if category.id != 3 %}
    <form action="" method="POST">{% csrf_token %}
        <div class="input-group">
            <span class="input-group-addon" id="" style="border:1px solid #ccc; border-radius: 4px;">{{ category.category_name }}</span>
            <input type="hidden" name="categoryId" id="categoryId" value="{{ category.id }}"/>
            <input type="submit" class="resAddBtn btn btn-danger" role="button" value="삭제"/>
        </div>
    </form>
    {% endif %}
    {% endfor %}
    ```

    6. 책에는 없지만, 보기에 좋지 않아서 `index.html`에서도 '기본 그룹'이 가장 먼저 나오도록 수정

    ```html
    <ul class="restaurantListDiv nav nav-pills nav-stacked">
        {% for category in categories %}
        {% if category.id == 3 %}
        <li class="category deactive">{{ category.category_name }}</li>
        <ul class="restaurantList">
    
            <div class="input-group">
                <span class="input-group-addon">
                    <input name="check1" id="check1" type="checkbox">
                </span>
                <a href="restaurantDetail/1"><input name="res1" id="res1" type="text" class="form-control" disabled style="cursor: pointer;" value="1"></a>
            </div>
    
            <div class="input-group">
                <span class="input-group-addon">
                    <input name="check2" id="check2" type="checkbox">
                </span>
                <a href="restaurantDetail/2"><input name="res2" id="res2" type="text" class="form-control" disabled style="cursor: pointer;" value="2"></a>
            </div>
    
        </ul>
        {% endif %}
        {% endfor %}
    
        {% for category in categories %}
        {% if category.id != 3 %}
        <li class="category deactive">{{ category.category_name }}</li>
        <ul class="restaurantList">
    
            <div class="input-group">
                <span class="input-group-addon">
                    <input name="check1" id="check1" type="checkbox">
                </span>
                <a href="restaurantDetail/1"><input name="res1" id="res1" type="text" class="form-control" disabled style="cursor: pointer;" value="1"></a>
            </div>
    
            <div class="input-group">
                <span class="input-group-addon">
                    <input name="check2" id="check2" type="checkbox">
                </span>
                <a href="restaurantDetail/2"><input name="res2" id="res2" type="text" class="form-control" disabled style="cursor: pointer;" value="2"></a>
            </div>
    
        </ul>
        {% endif %}
        {% endfor %}
    </ul>
    ```

#### Delete

카테고리 Delete 기능 구현

1. '삭제' 버튼을 누르면 `categoryCreate/delete` url로 이동하도록 하기 (`categoryCreate.html`)

```html
{% for category in categories %}
{% if category.id != 3 %}
<form action="./delete" method="POST">{% csrf_token %}
...
</form>
{% endif %}
{% endfor %}
```

2. `shareRes/urls.py` 수정

```python
# /shareRes/urls.py

# 추가한 코드
path('categoryCreate/delete', views.Delete_category, name='cateDelete'),
```

3. `shareRes/views.py`에 `Delete_category` 함수 추가

```python
# /shareRes/views.py

# 추가한 코드
def Delete_category(request):
    category_id = request.POST['categoryID']
    delete_category = Category.objects.get(id=category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))
```

### Restaurant

#### Create

'맛집 추가하기' 버튼을 눌렀을 때 나오는 페이지에서 식당을 입력받아 데이터 베이스에 추가하기

1. 카테고리 항목을 내가 추가한 카테고리로 변경 (`restaurantCreate.html`)

```python
# /shareRes/views.py

# 수정한 코드
def restaurantCreate(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, "shareRes/restaurantCreate.html", content)
```

```html
<span class="input-group-addon" id="sizing-addon2">카테고리</span>
<select id="resCategory" name="resCategory" class="resCategory" size="1" required autofocus>
    {% for category in categories %}
    {% if category.id == 3%}
    <option value="{{category.id}}" selected>{{category.category_name}}</option>
    {% endif %}
    {% endfor %}

    {% for category in categories %}
    {% if category.id != 3%}
    <option value="{{category.id}}">{{category.category_name}}</option>
    {% endif %}
    {% endfor %}
</select>
```

- '기본 그룹'이 선택된 상태로
- 책과 다르게 '기본 그룹'이 가장 위에 있는 카테고리로 보이게 설정

2. 식당 객체 생성 후 데이터베이스에 추가

``` python
# /shareRes/models.py

# 추가한 코드
class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=3)
    restaurant_name = models.CharField(max_length=100)
    restaurant_link = models.CharField(max_length=500)
    restaurant_content = models.TextField()
    restaurant_keyword = models.CharField(max_length=50)
```

- `models.ForeignKey()` : 다른 객체를 참조한다는 의미
  - `Category`를 참조 (`Category` 모델에 존재하는 데이터만 값으로 받는다는 의미)
- `on_delete=` : 참조하고 있는 모델이 삭제되었을 때 어떻게 할지 정하는 것, 예를 들어 카테고리1 안에 식당1, 식당2가 있다고 할 때 카테고리1을 삭제하면
  - `CASCADE` : 식당1, 식당2 모두 삭제
  - `PROTECT` : 식당1, 식당2가 카테고리1에 속하는 이상 카테고리1을 삭제할 수 없음
  - `SET_NULL` : 식당1, 식당2의 카테고리가 NULL로 설정됨
    - `null=True` 옵션을 더 추가해야함
  - `SET_DEFAULT` : `default=`으로 참조하는 id를 가진 카테고리로 설정됨, 나의 코드에서는 id가 3인 '기본 그룹'이 됨

3. cmd에서 migrate 반복
4. '맛집 추가' 버튼을 눌렀을 때 사용자가 넘긴 데이터를 받아 데이터베이스에 저장 (`restaurantCreate.html`)

```html
<form action="./create" method="POST" onsubmit="return checkFrom();">{% csrf_token %}
```

```python
# shareRes/urls.py

# 추가한 코드
path('restaurantCreate/create', views.Create_restaurant, name='resCreate'),
```

```python
# shareRes/views.py

# 추가한 코드
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
```





