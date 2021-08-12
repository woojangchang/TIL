from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from .models import *

# Create your views here.
def fileView(request):
    return render(request, 'main/uploadFile.html')

def upload(request):
    try:
        file = request.FILES['fileInput']

        origin_file_name = file.name
        user_id = request.session['user_id']
        now_HMS = datetime.today().strftime('%H%M%S')
        file_upload_name = now_HMS + '_' + user_id + '_' + origin_file_name
        file.name = file_upload_name
        user = User.objects.get(user_id = user_id)
        document = Document(file_path = file, file_name = origin_file_name, user_id=user)
        document.save()
    except:
        message = {'message':'파일 업로드에 실패했습니다.'}
        return render(request, 'main/error.html', message)
    return redirect('main_index')

def index(request):
    return redirect('fileView')