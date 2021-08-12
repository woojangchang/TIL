from upload.models import Document
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import *

import os
from django.conf import settings
import hashlib

# Create your views here.
def main(request):
    try:
        user_id = request.session['user_id']
        user_name = request.session['user_name']
        return redirect('main_index')
    except:
        return render(request, 'main/login.html')
        
def login(request):
    loginEmail = request.POST['loginEmail']
    loginPW = request.POST['loginPW']
    encoded_pw = loginPW.encode()
    encrypted_pw = hashlib.sha256(encoded_pw).hexdigest()
    try:
        user = User.objects.get(user_id = loginEmail)
    except:
        msg = '가입되지 않은 아이디입니다.'
        content = {'message':msg}
        return render(request, "main/error.html", content)

    # 사용자가 입력한 PW 암호화
    if user.user_pw == encrypted_pw and user.user_validation:
        request.session['user_name'] = user.user_name
        request.session['user_id'] = user.user_id
        return redirect('main_index')
    else:
        msg = '아이디 혹은 비밀번호가 틀렸습니다.'
        content = {'message':msg}
        return render(request, "main/error.html", content)

def error(request):
    return HttpResponse("error")

def index(request):
    if 'user_name' in request.session.keys():
        user_id = request.session['user_id']
        user = User.objects.get(user_id = user_id)
        documents = Document.objects.filter(user_id=user)
        content = {'documents':documents}
        return render(request, 'main/index.html', content)
    else:
        return redirect('main')

def download(request):
    path = request.GET['path']
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/liquid; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    
    else:
        message = '알 수 없는 오류가 발생했습니다.'
        return render(request, 'main/error.html', {'message':message})

def logout(request):
    del request.session['user_name']
    del request.session['user_id']
    return redirect('main')