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

## 1.5 Login / Logout

- 쿠키 : 사용자의 컴퓨터에 저장되어 브라우저가 종료되어도 인증이 유지됨
  - 키, 값, 유효시간, 도메인 등으로 구성
  - 로그인할 때 아이디, 비밀번호가 입력된 상태로 저장하는 방식
- 세션 : 서버에서 관리
  - 접속 시간에 제한을 두어 일정 시간 응답이 없으면 세션이 끊기게 함
  - 보안성은 높으나 반응 속도에서 쿠키보다 느림
- 따라서 views.py에서 쿠키로 저장한 유저 정보를 세션으로 넘기도록 변경
- main/views.py - 인증 코드 입력 후 유저가 로그인된 상태가 되게끔 유저 정보를 세션으로 넘겨줌

```python
response = redirect('main_index')
response.delete_cookie('code')
response.delete_cookie('user_id')
# response.set_cookie('user', user)
request.session['user_name'] = user.user_name
request.session['user_email'] = user.user_email
```

- signin.html

```html
<h3>안녕하세요. 로그인을 진행해주세요.</h3><br>
<form action="singin/login" method="POST">{% csrf_token %}
    <div class="input-group">
```

- main/urls.py

```python
path('signin/login', views.login, name='main_login'),
```

- main/views.py

```python
def login(request):
    loginEmail = request.POST['loginEmail']
    loginPW = request.POST['loginPW']
    user = User.objects.get(user_email = loginEmail)

    if user.user_password == loginPW:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else:
        return redirect('main_loginFail')
```

- 메인 화면은 로그인한 사람만 볼 수 있도록, 사용자 정보가 세션에 담겨 있으면 메인 화면, 아니면 회원 가입 페이지로 연결
- main/views.py

```python
def index(request):
    if 'user_name' in request.session.keys():
        return render(request, 'main/index.html')
    else:
        return redirect('main_signin')
    
def result(request):
    if 'user_name' in request.session.keys():
        return render(request, 'main/result.html')
    else:
        return redirect('main_signin')
```

- 세션 값은 딕셔너리 형태로 있기 때문에 key로 user name을 찾음
- main/urls.py - logout url 추가

```python
path('logout', views.logout, name='mian_logout'),
```

- main/views.py - logout 함수 추가

```python
def logout(request):
    del request.session['user_name']
    del request.session['user_email']
    return redirect('main_signin')
```

## 1.6 Upload File

- index.html - 파일 제출 버튼을 눌렀을 때의 url 등록

```html
<div class="fileInputDiv">
    <form action="calculate/" method="POST">{% csrf_token %}
        <div class="input-group">
```

- calculate/views.py - calculate 함수에서 파일 받아오기

```python
def calculate(request):
    file = request.POST['fileInput']
    return HttpResponse("calculate, calculate function")
```

- 파일을 업로드하면 오류가 난다고 하는데 난 나지 않는다...

```html
<form action="calculate/" method="POST" enctype="multipart/form-data">{% csrf_token %}
```

- enctype을 추가하라는데 하나 안 하나 똑같이 오류는 나지 않는다.
  - 쓰지 않으면 파일의 경로만 전송되고 파일 자체는 전송되지 않는다고 하는데 왜 오류는 안 나는지 모르겠다.
- calculate/views.py - FILES로 수정

```python
def calculate(request):
    file = request.FILES['fileInput']
    return HttpResponse("calculate, calculate function")
```

- 데이터베이스에 저장하는 방법은 Learn에서

## 1.7 Pandas

- calculate/views.py

```python
def calculate(request):
    doc = request.FILES
    # print(doc)
    file = doc['fileInput']
    # print('# 사용자가 등록한 파일의 이름 :', file)
    df = pd.read_excel(file, sheet_name='Sheet1', header=0)
    # print(df.head())
    grade_dic = {}
    email_domain_dic = {}
    total_row_num = len(df)
    for i in range(total_row_num):
        data = df.loc[i]
        if not data['grade'] in grade_dic.keys():
            grade_dic[data['grade']] = [data['value']]
        else:
            grade_dic[data['grade']].append(data['value'])
        
        email_domain = data['email'].split('@')[1]
        if not email_domain in email_domain_dic.keys():
            email_domain_dic[email_domain] = 1
        else:
            email_domain_dic[email_domain] += 1

    grade_calculate_dic = {}
    for key in grade_dic.keys():
        grade_calculate_dic[key] = {}
        grade_calculate_dic[key]['min'] = min(grade_dic[key])
        grade_calculate_dic[key]['max'] = max(grade_dic[key])
        grade_calculate_dic[key]['avg'] = float(sum(grade_dic[key]))/len(grade_dic[key])
    # 결과 출력
    grade_list = list(grade_calculate_dic.keys())
    grade_list.sort()
    for key in grade_list:
        print("# grade:",key)
        print("min:",grade_calculate_dic[key]['min'], end='')
        print("/ max:",grade_calculate_dic[key]['max'], end='')
        print(f"/ avg: {grade_calculate_dic[key]['avg']:.4f}", end='\n\n')
    
    print('## EMAIL 도메인별 사용 인원')
    for key in email_domain_dic.keys():
        print(f'# {key} : {email_domain_dic[key]}명')

    return HttpResponse("calculate, calculate function")
```

- 엑셀 파일로부터 grade별 점수 최소, 최대, 평균을 구하고 email 도메인별 사용 인원 확인

## 1.8 Complete Project

- 결과 페이지
- calculate/views.py

```python
grade_calculate_dic_to_session = {}
    for key in grade_list:
        grade_calculate_dic_to_session[int(key)] = {}
        grade_calculate_dic_to_session[int(key)]['max'] = {grade_calculate_dic[key]['max']}
        grade_calculate_dic_to_session[int(key)]['min'] = {grade_calculate_dic[key]['min']}
        grade_calculate_dic_to_session[int(key)]['avg'] = {grade_calculate_dic[key]['avg']}
    request.session['grade_calculate_dic'] = grade_calculate_dic_to_session
    request.session['email_domain_dic'] = email_domain_dic
    return redirect('/result')
```

- django에서는 numpy.int64 등의 자료형을 제대로 읽지 못함(?)
  - 책은 2.2.2 버전의 장고이지만, 3.2.4버전에서도 그런지는 모르겠으나 일단 책을 따라감
- main/views.py

```python
def result(request):
    if 'user_name' in request.session.keys():
        content = {}
        content['grade_calculate_dic'] = request.session['grade_calculate_dic']
        content['email_domain_dic'] = request.session['email_domain_dic']
        del request.session['grade_calculate_dic']
        del request.session['email_domain_dic']
        return render(request, 'main/result.html', content)
    else:
        return redirect('main_signin')
```

- 앞서 calculate/views.py에서 session으로 넘겨준 dict를 받아온 후 삭제
- result.html

```html
<h3> * Excel 결과 확인 *</h3>
<h4> - grade별 최솟값, 최댓값, 평균값</h4>
{% for key, value in grade_calculate_dic.items %}
<h5>GRADE : {{ key }}</h5>
<p><strong>최솟값 : </strong>{{ value.min }}</p>
<p><strong>최댓값 : </strong>{{ value.max }}</p>
<p><strong>평균값 : </strong>{{ value.avg }}</p>
<br>
{% endfor %}
<br>
<h4> - 이메일별 주소 도메인 인원</h4>
{% for key, value in email_domain_dic.items %}
<p><strong>{{ key }}: </strong>{{ value }}명</p>
{% endfor %}
<br>
```

- dictionary의 key를 []로 받는게 아닌 .으로 받음
- main/views.py - 로그인 실패 처리

```python
def login(request):
    loginEmail = request.POST['loginEmail']
    loginPW = request.POST['loginPW']
    try:
        user = User.objects.get(user_email = loginEmail)
    except:
        return redirect('main_loginFail')
    if user.user_password == loginPW and user.user_validate:
        request.session['user_name'] = user.user_name
        request.session['user_email'] = user.user_email
        return redirect('main_index')
    else:
        return redirect('main_loginFail')
```

- 등록된 이메일을 입력하지 않았다면 로그인 실패
- validate 하지 않은 유저도 로그인 실패 - 추후 validate 하지 않은 유저가 가입을 시도하면 기존 데이터 삭제 후 새로 데이터에 추가한 후 인증 코드 발송, validate한 유저의 이메일로 가입하면 가입 실패 경고 메세지 띄우기도 구현하면 좋을 것 같음
- main/urls.py

```python
path('loginFail', views.loginFail, name='main_loginFail'),
```

- main/views.py

```python
def loginFail(request):
    return render(request, 'main/loginFail.html')
```

- loginFail.html

```html
<html lang="ko">
<head>
    <meta charset="UTF-8">

    <!-- Boot strap -->
    <!-- 합쳐지고 최소화된 최신 CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <!-- 부가적인 테마 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">
    <!-- 합쳐지고 최소화된 최신 자바스크립트 -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

    <style>
        .panel-footer{
            height:10%;
            color:gray;
        }
    </style>
    <title>Excel Calculate</title>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="page-header">
                <a href="/" class="btn btn-default btn-xs" style="margin: 10px">메인화면</a>
                <h1>Excel Calculate <small>with Django</small></h1>
            </div>
        </div>
        <div class='body'>
            <h1>로그인 실패</h1>
            <h4>아이디 또는 비밀번호가 틀렸거나 인증되지 않은 아이디입니다. 로그인을 다시 시도해주세요.</h4>
            <a href="/signin" class="btn btn-success btn-xs" style="margin: 10px">로그인 하기</a>
        </div>
        <div class="panel-footer">
            실전예제로 배우는 Django. Project3-ExcelCalculate
        </div>
    </div>
</body>
</html>
```

