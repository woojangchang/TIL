from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

from random import randint
from main.models import *
import hashlib

# Create your views here.
def signup(request):
    return render(request, 'main/signup.html')

def email(request):
    verifyCode = randint(1000, 9999)
    name = request.POST['signupName']
    email = request.POST['signupEmail']
    pw = request.POST['signupPW']
    encoded_pw = pw.encode()
    encrypted_pw = hashlib.sha256(encoded_pw).hexdigest()
    try:
        user = User.objects.get(user_id=email)
        if not user.user_validation:
            user.delete()
        else:
            message = {'message':'이미 가입된 이메일입니다.'}
            return render(request, 'main/error.html', message)
    except:
        pass

    user = User(user_name=name, user_id=email, user_pw=encrypted_pw)
    user.save()
    response = redirect('verifyView')
    response.set_cookie('code', verifyCode)
    response.set_cookie('user_id', email)
    try:
        content = {'verifyCode':verifyCode}
        msg_html = render_to_string('signup/email_format.html', content)
        msg = EmailMessage(subject="인증 코드 발송 메일", body=msg_html,
        from_email="myemail@email.com",
        bcc=[email])
        msg.content_subtype = 'html'
        msg.send()
        return response
    except:
        message = {'message':'메일 전송에 실패했습니다.'}
        return render(request, 'main/error.html', message)

def verifyView(request):
    code = request.COOKIES.get('code')
    email = request.COOKIES.get('user_id')
    if code and email:
        return render(request, 'main/verifyCode.html')
    else:
        return redirect('main')

def verify(request):
    code = request.COOKIES.get('code')
    email = request.COOKIES.get('user_id')

    user_code = request.POST['verifyCode']

    if code == user_code:
        user = User.objects.get(user_id = email)
        user.user_validation = True
        user.save()

        response = redirect('verifyGood')
        response.delete_cookie('code')
        response.delete_cookie('user_id')

        request.session['user_name'] = user.user_name
        request.session['user_id'] = user.user_id
        return response
    else:
        msg = '입력한 코드를 다시 확인해 주세요.'
        content = {'msg':msg}
        return render(request, "main/verifyCode.html", content)

def verifyGood(request):
    return render(request, 'main/verifyGood.html')