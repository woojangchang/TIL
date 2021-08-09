from django.shortcuts import redirect, render
from .models import *
from random import *
from sendEmail.views import *

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def signup(request):
    return render(request, 'main/signup.html')

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

    send_result = send(email, code)
    if send_result:
        return response
    else:
        return HttpResponse("이메일 발송에 실패했습니다.")

def signin(request):
    return render(request, 'main/signin.html')

def verifyCode(request):
    return render(request, 'main/verifyCode.html')

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

def result(request):
    return render(request, 'main/result.html')