# Chapter 4

## 1.2 Start App

- 이전 2, 3장과 같이 app 생성 (main, sendEmail, calculate)

## 1.3 CRUD

- ./urls.py

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include('sendEmail.urls'), name='email'),
    path('calculate', include('calculate.urls'), name='calculate'),
    path('', include('main.urls'), name='main')
]
```

- ./sendEmail/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('send', views.send, name='email_send'),
]
```

- ./sendEmail/views.py

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def send(receiverEmail, verifyCode):
    return HttpResponse("sendEmail, send function")
```

- urls.py와 views.py는 항상 함께 수정해야 오류가 나지 않음
- 마찬가지로 calculate, main의 urls.py, views.py 수정
- `redirect()` : `HttpResponseRedirect()` 함수와 거의 동일
  - 차이점 : `HttpResponseRedirect(reverse('index'))` 처럼 reverse 함수로 특정 name을 가진 url을 가져왔다면, `redirect('main_index')` 처럼 model, view, url 등 다양한 것을 인자로 전달해 줄 수 있음
- superuser 생성을 하여 데이터를 쉽게 관리
  - `python manage.py migrate`
  - `python manage.py createsuperuser`

## 1.4 Register

- 순서
  1. 회원가입 화면에서 데이터를 받아 데이터베이스 저장, 인증되지 않은 유저로 등록
  2. 데이터베이스에 입력된 이메일로 인증코드 발송, 유저 이름과 함께 저장
  3. 인증 코드 입력 화면으로 전환
  4. 인증 코드와 입력된 코드와 비교하여 성공/실패 처리
  5. 성공하면 인증된 유저로 변경, 실패하면 회원 정보 삭제
- models.py

```python
from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)
    user_validate = models.BooleanField(default=False)
```

- user_email : id는 유일해야 하므로 unique=True
- user_validate : 입력되지 않아도 False로 저장
- 이후 migrate

- signup.html - 회원 가입 버튼 클릭 이동 url

```html
<h1> 회원가입 하기 </h1><br>
<form action="signup/join" method="POST" id="signup-form">{% csrf_token %}
    <div class="input-group">
        <span class="input-group-addon">이름</span>
```

- main/urls.py

```python
path('signup/join', views.join, name='main_join'),
```

- main/views.py - 데이터 베이스에 저장

```python
def join(request):
    print(request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name=name, user_email=email, user_password=pw)
    user.save()
    return redirect('main_verifyCode')
```

- main/admin.py - admin 페이지에 model 등록

```python
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
```

- main/views.py - join 함수에서 인증 코드 생성, 메일 발송

```python
def join(request):
    print(request)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    user = User(user_name=name, user_email=email, user_password=pw)
    user.save()

    code = randint(1000, 9999)
    response = redirect('main_verifyCode')
    response.set_cookie('code', code)
    response.set_cookie('user_id', user.id)
    return response
```

- 사이트 쿠키에 code, user_id를 남김
- 이후 send 함수 생성하여 join 함수에서 호출하여 이메일 전송
- sendEmail/templates/sendEmail/email_format.html - 이메일 내용 포맷

```html
<html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>ExcelCalculate 회원 가입</h1>
        <p>다음의 인증 코드를 입력해 주세요.</p>

        <h2>{{ verifyCode }}</h2>
    </body>
</html>
```

- sendEmail/views.py

```python
from django.http import HttpResponse
from django.shortcuts import render

from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def send(recieverEmail, verifyCode):
    try:
        content = {'verifyCode':verifyCode}
        msg_html = render_to_string('sendEmail/email_format.html', content)
        msg = EmailMessage(subject="인증 코드 발송 메일", body=msg_html,
        from_email="myemail@email.com",
        bcc=[recieverEmail])
        msg.content_subtype = 'html'
        msg.send()
        return True
    except:
        return False
```

- join 함수에서 호출할 것이기 때문에 request를 인자로 받지 않음
- settings.py에서 3장의 email 관련 코드를 똑같이 추가
- main/views.py에서 send 함수 호출

```python
	send_result = send(email, code)
    if send_result:
        return response
    else:
        return HttpResponse("이메일 발송에 실패했습니다.")
```

- verifyCode.html - verify url로 이동

```html
<h3>이메일로 전송된 메일의 인증코드를 입력해주세요.</h3><br>
<form action="verify" method="POST">{% csrf_token %}
    <div class="input-group">
```

- main/views.py - 사용자가 입력한 코드가 쿠키에 저장되어 있는 코드와 일치하면 id에 해당하는 user_validate 데이터를 True로 변경하며, 아니면 다시 코드 입력 페이지를 띄우기

```python
def verify(request):
    user_code = request.POST['verifyCode']
    cookie_code = request.COOKIES.get('code')
    if user_code == cookie_code:
        user = User.objects.get(id = request.COOKIES.get('user_id'))
        user.user_validate = True
        user.save()

        response = redirect('main_index')
        response.delete_cookie('code')
        response.delete_cookie('user_id')
        response.set_cookie('user', user)
        return response
    else:
        msg = '입력한 코드를 다시 확인해 주세요.'
        content = {'msg':msg}
        return render(request, "main/verifyCode.html", content)
```

- `request.COOKIES.get()` : join 함수에서 내보냈던 쿠키 name을 통해 value를 가져옴
- user_validate를 True로 변경
- 로그인한 유저의 정보(객체)를 쿠키로 저장
- 책 내용과 다르게, 입력한 코드가 틀렸으면 다시 입력하라는 경고 문구가 화면에 나오도록 수정
- verifyCode.html

```html
<h4>회원가입을 위해 입력하신 이메일로 인증코드를 보냈습니다.</h4>
<h3>이메일로 전송된 메일의 인증코드를 입력해주세요.</h3><br>
<h3 style="color:red">{{ msg }}</h3>
<form action="verify" method="POST">{% csrf_token %}
```

- 처음 접속하면 msg라는 변수가 없기 때문에 화면에 뜨지 않았다가 한 번 틀리면 msg가 생겨 화면에 출력

