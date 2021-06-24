도서 : Django 한그릇 뚝딱

# Django

## Environment

`conda deactivate`

`conda create --name django python=3.8.3`

`conda env list`

`conda activate django`

`pip install ipykernel`

`python -m ipykernel install --user --name django --display-name "Python Django"`

`conda install -c conda-forge jupyterlab`

## Installation

`pip install Django==3.2.4`

## Create Project

https://docs.djangoproject.com/ko/3.2/intro/tutorial01/

`django-admin startproject mysite`

- cmd창에 `python manage.py runserver` 입력 후 http://127.0.0.1:8000/ 로 접속했을 때 아래 화면이 나오면 설치 완료

![image-20210622104519007](README.assets/image-20210622104519007.png)



## Create App

- `manage.py`가 있는 폴더에서 `python manage.py startapp <appname>` 명령어를 실행하여 `<appname>` 앱을 생성한다.

- ```python
  # appname/views.py
  from django.http import HttpResponse
  
  def index(request):
      return HttpResponse("Hello, world. You're at the polls index.")
  ```

- ```python
  # appname/urls.py
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

- ```python
  # mysite/urls.py
  from django.contrib import admin
  from django.urls import include, path
  
  urlpatterns = [
      path('polls/', include('polls.urls')),
      path('admin/', admin.site.urls),
  ]
  ```

## Connect DB

https://docs.djangoproject.com/en/3.2/ref/settings/#databases

```python
# mysite/settings.py
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tips',
        'USER': 'root',
        'PASSWORD': '3756',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

- mysql에 등록되어 있는 `tips` 데이터베이스를 가져온다.

### Migration

- `pip install mysqlclient` 후 `python manage.py migrate`를 통해 mysql과 연결한다.

```mysql
# mysql
use tips;
show tables;
```

![image-20210622135316066](README.assets/image-20210622135316066.png)

성공했으면 위와 같은 테이블이 생성된다.



## Administration

1. `python manage.py createsuperuser` 로 admin id와 email, password를 등록하고 http://127.0.0.1:8000/admin/ 에 접속하여 등록한 id와 pw로 로그인하면 Django 관리창이 뜬다.
2. Add Users로 새로운 유저를 등록하면(꼭 하지 않아도 된다.) 서버와 연결된 mysql 데이터베이스 테이블의 `auth.user`에 유저 데이터가 등록되어 있는 것을 확인할 수 있다.



## Model

https://docs.djangoproject.com/ko/3.2/intro/tutorial02/

`views.py`, `urls.py` 등을 위 링크를 보고 수정을 거친 뒤

```shell
python manage.py shell
```

```python
from polls.models import Choice, Question
from django.utils import timezone

q = Question(question_text="Q", pub_date=timezone.now())

q.choice_set.create(choice_text='V1', votes=0)
q.choice_set.create(choice_text='V2', votes=0)
```

위와 같은 과정을 거치면 url에 투표창이 생성된다.

