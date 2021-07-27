# Index

* [1.1 Create Project](#11-create-project)
* [1.2 Configure Application](#12-configure-application)
* [1.3 Set URL](#13-set-url)
* [1.4 Use HTML Template](#14-use-html-template)
* [1.5 MVC](#15-mvc)
  + [Model](#model)
  + [User to Server](#user-to-server)
  + [Server to Database](#server-to-database)
  + [Database to Server](#database-to-server)
  + [Server to User](#server-to-user)
* [1.6 CRUD](#16-crud)
* [2.1 Why, How to split APPs](#21-why--how-to-split-apps)
* [2.2 MVC](#22-mvc)
  + [Model](#model-1)
  + [View](#view)
  + [Controller](#controller)
* [2.3 CRUD](#23-crud)
* [2.4 Develop App by Myself](#24-develop-app-by-myself)

# Chapter 2

## 1.1 Create Project

Prompt(cmd)에서

- `django-admin startproject ToDoList`
  - `ToDoList` : 본인이 만들 프로젝트명을 입력

## 1.2 Configure Application

- `python manage.py startapp my_to_do_app`
  - `my_to_do_app` : 본인이 구성할 어플리케이션명을 입력

```python
# ToDoList/ToDoList/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_to_do_list' # 추가해야할 코드
]
```

- 새로운 app을 만들 때마다 꼭 추가해야함

## 1.3 Set URL

- `python manage.py runserver`
  - 기본적으로 127.0.0.1:8000 or localhost:8000 으로 접속

```python
# ToDoList/ToDoList/urls.py
from django.contrib import admin
from django.urls import path, include # 추가해야할 코드

urlpatterns = [
    path('', include('my_to_do_app.urls')), # 추가해야할 코드
    path('admin/', admin.site.urls),
]
```

- localhost:8000/admin/ 이라는 주소로 접근했을 때, `admin.site.urls` 로 접근하라는 의미
- `admin.site.urls` 와 달리 `include('my_to_do_app.urls')`로 쓰는 이유 : 내가 직접 새롭게 추가한 app이기 때문

```python
# 직접 urls.py 파일을 생성해야함
# ToDoList/my_to_do_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
```

- 같은 폴더의 `views.py`의 `index` 함수를 처리하도록 함

```python
# ToDoList/my_to_do_app/views.py
from django.shortcuts import render
from django.http import HttpResponse # 추가해야할 코드

# Create your views here.
# 추가해야할 index 함수
def index(request):
    return HttpResponse('my_to_do_app first page')
```

- 이후 cmd로 ToDoList 폴더에서 `python manage.py runserver`를 한 뒤 localhost:8000/에 접속하면 아래와 같은 화면이 뜬다.

![image-20210706220828088](C:\Users\master\TIL\Django\README.assets\image-20210706220828088.png)

## 1.4 Use HTML Template

- `my_to_do_app` 폴더에 `templates` 폴더를 생성한 뒤 그 안에 또다시 `my_to_do_app` 폴더를 생성한다.
- HTML 파일을 템플릿으로 사용하려면 해당 앱의 `templates` 폴더의 앱과 동일한 이름을 가진 폴더의 html 파일을 불러온다.
- html 파일을 생성한 이후 `views.py` 파일을 수정해야한다.

```python
# ToDoList/my_to_do_app/views.py

# 수정한 코드
def index(request):
    return render(request, 'my_to_do_app/index.html')
```

- 사용자가 특정 url에 접근해서 index 함수를 실행할 때, request를 받아와 user나 session과 같은 값들을 참조, render를 통해 사용자가 그대로 받아볼 수 있게 된다.

## 1.5 MVC

- Model, View, Controller
- Model : 데이터, 알고리즘 등
  - `my_to_do_app/models.py`
- View : 사용자에게 보여주는 것
  - `my_to_do_app/templates/`
- Controller : Model과 View를 컨트롤
  - `my_to_do_app/views.py`

### Model

- 데이터 베이스 생성

```python
# ToDoList/my_to_do_app/models.py
from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length=255)
```

- 장고에서 하나의 모델(데이터 테이블)은 class
  - class 안의 데이터 명이 content인 것이 CharField 형태이며 최대 길이 255자
- 이후 cmd에서 `manage.py`가 있는 폴더에서 `python manage.py makemigrations` 명령어를 입력
  - `migrations/0001_initial.py` 생성
- `python manage.py migrate`로 데이터 베이스 생성
  - 기본 데이터베이스인 sqlite에 저장
  - `python manage.py dbshell`로 데이터베이스에 접근 가능
    - `.tables` : 데이터베이스의 테이블 확인
    - `PRAGMA table_info(my_to_do_app_todo);` : 데이터 정보
      - 순서 | 이름 | 형태 | notnull 여부 | pk 여부
    - `select * from my_to_do_app_todo;` : 데이터 내용 확인

### User to Server

- html 화면에서 Todo를 입력하고 버튼을 누르면 데이터베이스에 저장되도록 하는 것이 목표

- `templates/my_to_do_app/index.html`의 첫줄 수정

```html
<form action="./createTodo/" method="POST">{% csrf_token %}
    <div class="input-group">
        <input id="todoContent" name="todoContent" type="text" class="form-control" placeholder="메모할 내용을 적어주세요">
        <span class="input-group-btn">
            <button class="btn btn-default" type="submit">메모하기!</button>
        </span>
    </div>
</form>
```

- `method="POST"` 방식에서는 `{% csrf_token %}`를 입력해줘야함

- `action="./createTodo/"` : action에 적힌 경로로 데이터가 전달됨

- `python manage.py runserver` 이후 메모하기 버튼을 클릭하면 404 error가 뜸

  - 제일 먼저 확인해야하는 것은 `ToDoList/urls.py`

  - ```python
    urlpatterns = [
        path('', include('my_to_do_app.urls')),
        path('admin/', admin.site.urls),
    ]
    ```

    위 코드를 통해 `my_to_do_app/urls.py`로 처리를 넘기도록 했기 때문에 그 파일을 확인

  - ```python
    # ToDoList/my_to_do_app/urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('', views.index),
        path('createTodo/', views.createTodo) # 추가한 코드
    ]
    ```

  - 그리고 `views.py`에서 `createTodo` 함수 생성

    ```python
    # ToDoList/my_to_do_app/views.py
    
    from django.shortcuts import render
    from django.http import HttpResponse
    
    # Create your views here.
    def index(request):
        return render(request, 'my_to_do_app/index.html')
    
    # 추가한 코드
    def createTodo(request):
        return HttpResponse('createTodo')
    ```

### Server to Database

- 문자열 입력 > 서버로 전송 : html 파일의 form의 역할
- 서버 > 데이터 베이스로 전송 : `createTodo` 함수의 request가 그 역할을 하며, html 파일의 `form`- `input`의 `name` attribute를 사용한다.

```python
# ToDoList/my_to_do_app/views.py

# 수정한 코드
def createTodo(request):
    user_input_str = request.POST['todoContent']
    return HttpResponse('createTodo => '+ user_input_str)
```

- request에서 POST에 접근해 `input` tag의 `name` attribute value인 'todoContent'를 통해 문자열을 받아옴

```python
# ToDoList/my_to_do_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import * # 추가한 코드

def createTodo(request):
    user_input_str = request.POST['todoContent']
    
    # 추가한 코드
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    
    return HttpResponse('createTodo => '+ user_input_str)
```

- 앞서 `models.py`에서 정의한 `Todo` class를 `createTodo` 함수에서 불러와 서버에서 받은 데이터를 데이터베이스에 저장한다.
- `python manage.py dbshell` > `select * from my_to_do_app_todo;`를 통해 데이터가 입력된 것을 확인할 수 있다.

### Database to Server

```python
# ToDoList/my_to_do_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo') # 수정한 코드
]
```

- url 대신 name을 이용해서 접근할 수 있도록 함

```python
# ToDoList/my_to_do_app/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect # 수정한 코드
from django.urls import reverse # 추가한 코드
from .models import *

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index')) # 수정한 코드
```

- `reverse('index')` : index라는 이름의 url을 찾음
  - 앞서 `urls.py`에서 추가한 `name=` 코드가 여기서 쓰인다.
- `HttpResponseRedirect()` : `reverse` 함수로 가져온 url로 이동

### Server to User

```python
# ToDoList/my_to_do_app/views.py

# Create your views here.
def index(request):
    # 추가한 코드
    todos = Todo.objects.all()
    content = {'todos':todos}
    
    return render(request, 'my_to_do_app/index.html', content)
```

- `Todo.objects.all()` : Todo 모델의 모든 데이터를 가져옴

```html
<div class="toDoDiv">
    <ul class="list-group">
        {% for todo in todos %}
        <form action="" method="GET">
            <div class="input-group" name='todo1'>
                <li class="list-group-item">{{ todo.content }}</li>
                <input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>
            <span class="input-group-addon">
                <button type="submit" class="custom-btn btn btn-danger">완료</button>
            </span>
            </div>
        </form>
    {% endfor %}
    </ul>
</div>
```

- `{% for todo in todos %}` : html 안에서 파이썬 문법 사용
- `views.py`에서 `render(..., content)`로 content dictionary를 넘겨주었지만 html에서는 content의 key를 바로 불러올 수 있음
  - 그렇기 때문에 todos라는 key를 바로 사용
- `{{ todo.content }}` : `{% %}`와 달리 사용자에게 보여지는 코드, 앞선 for문으로 불러온 todo(`models.py`에서 만든 Todo 객체)의 content 값

## 1.6 CRUD

- Create, Read, Update, Delete
- 데이터베이스에 데이터가 저장될 때 자동으로 주어지는 id는 unique하기 때문에 데이터를 지우고 싶다면 이 id를 통해야한다.
- `index.html`에서 input type hidden으로 `todo.id`를 value값으로 하고 있다.

```html
<div class="toDoDiv">
    <ul class="list-group">
        {% for todo in todos %}
        <form action="./deleteTodo/" method="GET">
            <div class="input-group" name='todo1'>
                <li class="list-group-item">{{ todo.content }}</li>
                <input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>
            <span class="input-group-addon">
                <button type="submit" class="custom-btn btn btn-danger">완료</button>
            </span>
            </div>
        </form>
    {% endfor %}
    </ul>
</div>
```

- `<form action="./deleteTodo/" method="GET">` : 완료 버튼을 누르면 deleteTodo url로 이동

```python
# ToDoList/my_to_do_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.createTodo, name='createTodo'),
    path('deleteTodo/', views.doneTodo, name='deleteTodo') # 추가한 코드
]
```

```python
# ToDoList/my_to_do_app/views.py

# 추가한 코드
def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    return HttpResponseRedirect(reverse('index'))
```

- `index.html`에서 값을 넘길 때 GET 방식을 썼으므로 `.GET` 메서드 이용
- `request.GET['todoNum']` : name이 `todoNum`인 것의 value를 가져옴

```python
# ToDoList/my_to_do_app/views.py
def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    
    # 추가한 코드
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()
    
    return HttpResponseRedirect(reverse('index'))
```

- `Todo.objects.get(id=done_todo_id)` : id를 참조하여 해당 id를 갖고 있는 객체를 데이터베이스에서 불러옴

## 2.1 Why, How to split APPs

- Why
  - 추후 동일한 기능 개발할 때 복붙하면 됨
  - 오류 발생 시 수정이 편함
- How
  - 명확한 기준은 없음, 개발자 마음대로
  - 여러 프로젝트 진행 시, 공통된 기능(로그인 등) 정도

## 2.2 MVC

- 사용자에게 보이는 화면과 내부적으로 계산되는 로직을 나눠 개발하는 방식
  - 보이는 화면 : `templates/.../index.html`
  - 내부적으로 계산되는 로직 : `views.py`

### Model

- Django에서 model은 `models.py`가 한다.
- 데이터 정의하는 종류 (`from django.db import models`)
  - `CharField` : 문자열, `max_length`로 최대 길이 지정가능, 쓰지 않으면 제한 없음
  - `DateField` : python datetime 라이브러리 형태의 날짜, 게시글이나 데이터의 등록 시간, 수정 시간 등을 표시하기 위할 때 사용
  - `EmailField` : EmailValidator라는 것을 통해 이메일 형식인지 확인하여 아니면 데이터 저장 중에 오류 발생
    - html에서 `input type='email'`을 하면 제출 자체가 되지 않으므로 오류를 막을 수 있다.
  - `FileField` : 파일을 저장할 수 있는 데이터 타입으로 `upload_to` 옵션으로 위치 지정 가능
  - `TextField` : 텍스트, `CharField`와 달리 최대 길이 지정 불가능(글자수에 제한이 없음)
  - `IntegerField` : 숫자형, 조회수, 추천 수 등
  - `BooldeanField` : True/False

### View

- Django에서 View 역할은 `templates` 폴더 내 각각의 html 파일이 한다.
- `appname/templates/appname/` 폴더를 생성한 뒤 html 파일을 저장한 이유 : 여러 앱 내에서 같은 이름의 html 파일을 쓰는 경우가 생길 수도 있기 때문

### Controller

- Django에서 Controller의 역할은 `views.py`가 한다.
- 함수를 정의하여 로직을 처리하도록 함
- `urls.py`에서 어떤 함수로 처리를 넘길 것인지 지정
- 인자 `request` : 웹에서 요청을 받아 데이터나 상태 값들이 포함되어 함수로 전달됨

## 2.3 CRUD

- Create

  1. 메모하기를 누르면 입력된 데이터와 함께 html 파일에서 설정한 `./createTodo/` url로 넘어간다.
  2. `urls.py`에서 `createTodo/` url로 넘어가면 `views.py`의 `createTodo` 함수가 기능하도록 한다.
  3. `views.py`의 `createTodo` 함수가 실행되면 1에서 받아온 데이터를 넘겨받아 `models.py`의 `Todo` 객체에 값을 넣고 데이터베이스에 저장한 뒤 `index`라는 이름을 가진 기본 도메인으로 돌아온다.

  - 일련의 과정은 매우 빠르게 진행되므로 createTodo url에 접속한 것을 유저는 확인하지 못한다.

- Delete

  1. 완료를 누르면 todoNum 번호와 함께 html 파일에서 설정한 `./deleteTodo/` url로 넘어간다.
  2. `urls.py`에서 `deleteTodo/` url로 넘어가면 `view.py`의 `doneTodo` 함수가 기능하도록 한다.
  3. `views.py`의 `doneTodo` 함수가 실행되면 1에서 받아온 데이터 번호로 해당 객체를 호출하여 삭제한 뒤 `index`라는 이름을 가진 기본 도메인으로 돌아온다.

- `GET`과 `POST`의 차이점

  - 보통 데이터를 생성하거나 삭제할 때는 `POST` 방식을 주로 사용하지만 정해진 규칙은 없다.
  - `GET`은 주소 값에 전달되는 값이 표시되며 보안에 취약, 길이 제한이 있고 전송 속도는 빠른 편
  - `POST`는 주소 값에 전달되는 값이 표시되지 않고 보안에 우수하며 데이터를 body 안에 포함시켜 서버에 전달하기 때문에 복잡한 형태의 데이터도 전송 가능

## 2.4 Develop App by Myself

**과제** : 완료 버튼을 눌렀을 때, 데이터가 삭제되는 것이 아닌, 보이지 않게만 하기

**해결 과정**

1. `models.py` 파일에 `isDone` 값을 생성하여 데이터베이스에 저장, 생성하는 데이터 종류는 Boolean형

   ```python
   # models.py
   class Todo(models.Model):
       content = models.CharField(max_length=255)
       isDone = models.BooleanField(default=False) # 추가한 코드
   ```

   - `python manage.py makemigrations`
   - `python manage.py migrate`

2. `views.py`의 `doneTodo` 함수를 수정하여 사용자가 완료 버튼을 클릭하면 `isDone` 값이 True가 되게 변경

   ```python
   # urls.py
   urlpatterns = [
       path('', views.index, name='index'),
       path('createTodo/', views.createTodo, name='createTodo'),
       path('doneTodo/', views.doneTodo, name='doneTodo')
   ] # 수정한 코드
   ```

   ```python
   # views.py
   def doneTodo(request):
       done_todo_id = request.GET['todoNum']
       print('완료한 todo의 id', done_todo_id)
       todo = Todo.objects.get(id=done_todo_id)
       
       # 수정한 코드
       todo.isDone = True
       todo.save()
       
       return HttpResponseRedirect(reverse('index'))
   ```

   - `todo.isDone = True` : `todo` 객체의 `isDone` 값을 True로

3. `isDone` 값이 False일 때만 값이 출력되도록 `index.html` 파일 수정

   ```html
   {% for todo in todos %}
   {% if todo.isDone == False %}
   <form action="./doneTodo/" method="GET">
       <div class="input-group" name='todo1'>
           <li class="list-group-item">{{ todo.content }}</li>
           <input type="hidden" id="todoNum" name="todoNum" value="{{ todo.id }}"></input>
       <span class="input-group-addon">
           <button type="submit" class="custom-btn btn btn-danger">완료</button>
       </span>
       </div>
   </form>
   {% endif %}
   {% endfor %}
   ```

   - `action`의 url을 `doneTodo/`로 수정
   - `{% %}`로 if문을 넣어 `isDone == False`를 확인
   - 책에서는 `{% endif %}` 이전에 `{% else %}`를 썼지만 굳이 없어도 된다.

