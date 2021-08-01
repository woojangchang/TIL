- [Chapter 3](#chapter-3)
  * [1.2 SET URLs and Templates](#12-set-urls-and-templates)
  * [1.3 CRUD](#13-crud)
    + [Category](#category)
      - [Create](#create)
      - [Read](#read)
      - [Delete](#delete)
    + [Restaurant](#restaurant)
      - [Create](#create-1)
      - [Read](#read-1)
      - [Update](#update)
      - [Delete](#delete-1)
  * [1.4 Send Email](#14-send-email)
  * [2.1 How to Use Sending Email](#21-how-to-use-sending-email)
  * [2.4 Develop App by Myself](#24-develop-app-by-myself)

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
    category_id = request.POST['categoryId']
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
  - `SET()` : SET에 설정된 함수를 실행시켜 참조하는 값이 되게 함
  - `DO_NOTHING` : 아무것도 하지 않음

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

#### Read

각 카테고리별로 속해있는 식당 목록 출력하기

1. 메인 페이지에서 식당 목록 데이터 불러오기

```python
# shareRes/views.py

# 수정한 코드
def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories': categories, 'restaurants':restaurants}
    return render(request, 'shareRes/index.html', content)
```

2. html 파일을 수정하여 카테고리별 식당 목록데이터 출력 (`index.html`)

```html
<ul class="restaurantList">

    {% for restaurant in restaurants %}
    {% if restaurant.category == category %}
    <div class="input-group">
        <span class="input-group-addon">
            <input name="checks" id="check{{restaurant.id}}" type="checkbox" value={{restaurant.id}}>
        </span>
        <a href="restaurantDetail/{{restaurant.id}}"><input name="res{{restaurant.id}}" id="res{{restaurant.id}}" 
                                                            type="text" class="form-control" disabled style="cursor: pointer;" value="{{restaurant.restaurant_name}}"></a>
    </div>
    {% endif %}
    {% endfor %}

</ul>
```

3. 식당을 클릭하면 상세 페이지로 이동하여 상세 정보 출력 (`restaurantDetail.html`)
   - 위 2번 코드의 `<a href="restaurantDetail/{{restaurant.id}}">`가 그 역할을 함

```python
# shareRes/urls.py

# 수정한 코드
path('restaurantDetail/<str:res_id>', views.restaurantDetail, name='resDetailPage'),
```

- `<str:res_id>` : 동적인 값
  - `str:`은 데이터 타입
  - `res_id`은 서버에서 받는 데이터 이름

```python
# shareRes/views.py

# 수정한 코드
def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'restaurant':restaurant}
    return render(request, "shareRes/restaurantDetail.html", content)
```

- `urls.py`에서 받은 `res_id`로 식당 정보를 가져오고 html로 넘겨줌

```html
<div class="input-group">
    <span class="input-group-addon" id="sizing-addon2">카테고리</span>
    <input id="resCategory" name="resCategory" type="text" class="form-control" disabled value="{{restaurant.category.category_name}}">
</div>
<div class="input-group">
    <span class="input-group-addon" id="sizing-addon2">맛집 이름</span>
    <input id="resTitle" name="resTitle" type="text" class="form-control" disabled value="{{restaurant.restaurant_name}}">
</div>
<div class="input-group">
    <span class="input-group-addon" id="sizing-addon2">관련 링크</span>
    <input id="resLink" name="resLink" type="text" class="form-control" disabled value="{{restaurant.restaurant_link}}">
</div>
<div class="input-group">
    <span class="input-group-addon" id="sizing-addon2">상세 내용</span>
    <textarea id="resContent" name="resContent" cols="90" rows="10" disabled value="">{{restaurant.restaurant_content}}</textarea>
</div>
<div class="input-group">
    <span class="input-group-addon" id="sizing-addon2">장소 키워드</span>
    <input id="resLoc" name="resLoc" type="text" class="form-control" disabled value="{{restaurant.restaurant_keyword}}">
</div>
```

- input type이 `text`인 나머지와는 달리 `textarea`인 상세 내용은 value에 값을 주는 게 아닌 `<textarea>`와 `</textarea>` 사이에 값을 줘야 출력이 된다.

#### Update

식당 상세 페이지에서 수정하기

1. 수정하기 버튼 추가 (`restaurantDetail.html`)

```html
<a href ="/" class="resAddBtn btn btn-info" role="button">홈으로</a>
<a href ="./updatePage/{{restaurant.id}}" class="resAddBtn btn btn-danger" role="button">수정하기</a>
```

2. 수정할 페이지 생성

```python
# shareRes/urls.py

# 추가한 코드
path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name='resUpdatePage'),
```

```python
# shareRes/views.py

# 추가한 코드
def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, "shareRes/restaurantUpdate.html", content)
```

- `restaurantCreate.html`을 복사, 붙여넣기 하여 `restaurantUpdate.html`로 수정, 제목을 `맛집 수정하기`로 고침

3. 수정할 식당의 기존 데이터 불러와서 출력하기 (`restaurantUpdate.html`)

```python
# shareRes/views.py

# 수정한 코드
def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    restaurant = Restaurant.objects.get(id=res_id)
    content = {'categories': categories, 'restaurant':restaurant}
    return render(request, "shareRes/restaurantUpdate.html", content)
```

4. 맛집 수정하기 페이지에서 '맛집 수정' 버튼을 눌렀을 때, 입력된 데이터가 수정할 식당 id가 일치하는 식당의 데이터에 업데이트

- `<input type="hidden" id="resId" name="resId" value="{{restaurant.id}}"/>`으로 식당의 id 데이터도 받음

```python
# shareRes/urls.py

# 추가한 코드
path('restaurantDetail/updatePage/update', views.Update_restaurant, name='resUpdate'),
path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name='resUpdatePage'),
```

- 위 순서로 코드가 진행되어야 하며, 반대로 있을 경우 `update` 페이지로 넘어가는 것이 아닌 res_id가 update인 페이지로 넘어가게 되어 오류가 발생한다.

```python
# shareRes/views.py

# 추가한 코드
def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    change_category = Category.objects.get(id=change_category_id)
    change_name = request.POST['resTitle']
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']

    before_restaurant = Restaurant.objects.get(id=resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))
```

- `HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))` : `<str:res_id>`에 값을 채우는 역할

#### Delete

식당 상세 페이지에서 삭제하기

1. 삭제하기 버튼 추가 (`restaurantDetail.html`)

```html
<form action="./delete" method="POST">{% csrf_token %}
    <input type="hidden" id="resId" name="resId" value="{{ restaurant.id }}"/>
    <input type="submit" class="resAddBtn btn btn-danger" value="삭제하기">
</form>
```

2. url 페이지 생성 및 삭제하는 함수 생성

```python
# shareRes/urls.py

# 추가한 코드
path('restaurantDetail/delete', views.Delete_restaurant, name='resDelete'),
```

```python
# shareRes/views.py

# 추가한 코드
def Delete_restaurant(request):
    res_id = request.POST['resId']
    restaurant = Restaurant.objects.get(id=res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))
```

## 1.4 Send Email

- 준비물 : 구글 계정, smtplib, email 라이브러리
  - SMTP : Simple Mail Transfer Protocol

1. 발송 버튼을 눌렀을 때 이동할 url 생성 (`index.html`)

```html
<form action="./sendEmail/send/" method="POST" onsubmit="return emailCheckForm();"> {% csrf_token %}
```

2. 발송 버튼을 누른 뒤 홈화면으로 돌아오도록 설정

```python
# sendEmail/views.py

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def sendEmail(request):
    return HttpResponseRedirect(reverse('index'))
```

3. 체크된 맛집에 대한 데이터 가져오기
   - 장고에서는 html에 같은 name의 checkbox가 여럿 있으면, 체크된 항목만 가져오도록 알아서 처리해준다.

```python
# sendEmail/views.py

# 수정한 코드
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    print(checked_res_list, '/', inputReceiver, '/', inputTitle, '/', inputContent)
    return HttpResponseRedirect(reverse('index'))
```

- `request.POST.getlist('checks')` : `checks`라는 name을 가진 항목들의 value를 list 형태로 반환

4. 사용자가 선택한 맛집 정보와 입력한 인사말을 이용해 이메일 본문 작성

- 이메일 본문은 html 형태로 만들어야 함

```python
# sendEmail/views.py

# 수정한 코드
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>" + inputContent + "</p>"
    mail_html += "공유한 맛집 리스트"
    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id=checked_res_id)
        mail_html += "<h2>" + restaurant.restaurant_name + "</h2>"
        mail_html += "<h4>* 관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"
        mail_html += "<h4>* 상세 내용</h4>" + "<p>" + restaurant.restaurant_content + "</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
        mail_html += "<br>"
    mail_html += "</body></html>"
    # print(mail_html)
    return HttpResponseRedirect(reverse('index'))
```

5. 이메일 발송

- 구글링을 통해 알아내는 것도 실력
- python으로 이메일 보내는 전반적인 방법 : [stackoverflow](https://stackoverflow.com/questions/882712/sending-html-email-using-python)
- 구글 SMTP 서버를 이용하여 이메일을 보내는 방법 : [stackabuse](https://stackabuse.com/how-to-send-emails-with-gmail-using-python)
- 구글 - 구글 계정 관리 - 보안 - 보안 수준이 낮은 앱의 액세스 - 허용을 차례대로 클릭하여 python에서 이메일을 보낼 수 있도록 설정

```python
# sendEmail/views.py

# 추가한 코드
from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json')
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        # print('check :', secrets[setting])
        return secrets[setting]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(setting)
        raise ImproperlyConfigured(error_msg)

# Create your views here.
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>" + inputContent + "</p>"
    mail_html += "공유한 맛집 리스트"
    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id=checked_res_id)
        mail_html += "<h2>" + restaurant.restaurant_name + "</h2>"
        mail_html += "<h4>* 관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"
        mail_html += "<h4>* 상세 내용</h4>" + "<p>" + restaurant.restaurant_content + "</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
        mail_html += "<br>"
    mail_html += "</body></html>"
    # print(mail_html)

    # smtp
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    id = get_secret('id')
    pw = get_secret('pw')
    server.login(id, pw)

    # msg
    msg = MIMEMultipart('alternative')
    msg['Subject'] = inputTitle
    msg['From'] = id
    msg['To'] = inputReceiver
    mail_html = MIMEText(mail_html, 'html')
    msg.attach(mail_html)
    # print(msg['To'], type(msg['To']))
    server.sendmail(msg['From'], msg['To'].split(','), msg.as_string()) # 받는 사람 여럿일 때 split
    server.quit()
    return HttpResponseRedirect(reverse('index'))
```

- 구글 계정 노출을 막기 위해, 장고 secret key를 숨겼던 secrets.json에 id와 pw를 숨김

## 2.1 How to Use Sending Email

- smtplib이 아닌 django 자체 이메일 시스템 이용
- django의 `send_mail` 함수
  - `message` 옵션이 string이므로, `render_to_string` 함수를 이용하여 html template를 문자열처럼 사용 가능

```python
# sendEmail/views.py
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    id = get_secret('id')
    pw = get_secret('pw')

    restaurants = []
    for checked_res_id in checked_res_list:
        restaurants.append(Restaurant.objects.get(id=checked_res_id))

    content = {'inputContent':inputContent, 'restaurants':restaurants}
    msg_html = render_to_string('sendEmail/email_format.html', content)

    msg = EmailMessage(subject=inputTitle, body=msg_html, from_email=id,
                        bcc=inputReceiver.split(','))
    msg.content_subtype = 'html'
    msg.send()
   	return HttpResponseRedirect(reverse('index'))
```

- `sendEmail/templates/sendEmail/email_format.html` 생성

```html
<html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>맛집 공유</h1>
        <p>{{ inputContent }}<br>공유한 맛집</p>
        {% for restaurant in restaurants %}
        <h2>{{restaurant.restaurant_name}}</h2>
        <h4>* 관련 링크</h4><p>{{restaurant.restaurant_link}}</p>
        <h4>* 관련 내용</h4><p>{{restaurant.restaurant_content}}</p>
        <h4>* 관련 키워드</h4><p>{{restaurant.restaurant_keyword}}</p>
        {% endfor %}
    </body>
</html>
```

- smtp 서버 설정
  - 하지 않을 경우, 컴퓨터 자체를 서버로 인식하여 메일 전송을 시도하여 오류가 남

```python
# settings.py

# Email Settings
EMIAL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = get_secret('id')
EMAIL_HOST_PASSWORD = get_secret('pw')
```

- `pythonanywhere`로 배포할 경우, `ALLOWED_HOSTS = ['account.pythonanywhere.com', '127.0.0.1', 'localhost']` 코드를 추가

## 2.4 Develop App by Myself

과제 : 이메일 발송버튼을 눌렀을 때, 정상적으로 발송되면 발송에 성공했다는 창으로, 실패했다면 실패했다는 창으로 연결되게 하며 홈으로 돌아가기 버튼을 추가하기

1. `sendSuccess.html`, `sendFail.html` 생성

```html
<html>
    <head>
        <title>발송 성공</title>
        <style>
            .result {
                background-color: bisque;
                margin:20px;
                padding:20px;
                text-align: center;
                font-size: 30px;
            }

            .tohome {
                text-align: center;
            }

            .btn {
                background-color: #f44336;
                color: white;
                padding: 10px 10px;
                text-decoration: none;
                display: inline-block;
            }
        </style>
    </head>

    <body>
        <div class="result">
            <h1>이메일 발송 결과</h1>
        </div>
        <div class="tohome">
            <h2>이메일 발송에 성공했습니다.</h2>
            <a href ="/" class="btn" role="button"><b>홈으로</b></a>
        </div>

    </body>
</html>
```

2. `views.py`에 성공, 실패 각각 따로 해당 url에 전송

```python
# sendEamil/views.py

# 수정한 코드
def sendEmail(request):
    try:
        checked_res_list = request.POST.getlist('checks')
        inputReceiver = request.POST['inputReceiver']
        inputTitle = request.POST['inputTitle']
        inputContent = request.POST['inputContent']

        id = get_secret('id')
        # pw = get_secret('pw')

        restaurants = []
        for checked_res_id in checked_res_list:
            restaurants.append(Restaurant.objects.get(id=checked_res_id))

        content = {'inputContent':inputContent, 'restaurants':restaurants}
        msg_html = render_to_string('sendEmail/email_format.html', content)

        msg = EmailMessage(subject=inputTitle, body=msg_html, from_email=id,
                            bcc=inputReceiver.split(','))
        msg.content_subtype = 'html'
        msg.send()
        return render(request, 'sendEmail/sendSuccess.html')
    
    except:
        return render(request, 'sendEmail/sendFail.html')
```

