from shareRes.models import Restaurant
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
import os
import json
from django.core.exceptions import ImproperlyConfigured

from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string

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

    # mail_html = "<html><body>"
    # mail_html += "<h1> 맛집 공유 </h1>"
    # mail_html += "<p>" + inputContent + "</p>"
    # mail_html += "공유한 맛집 리스트"
    # for checked_res_id in checked_res_list:
    #     restaurant = Restaurant.objects.get(id=checked_res_id)
    #     mail_html += "<h2>" + restaurant.restaurant_name + "</h2>"
    #     mail_html += "<h4>* 관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"
    #     mail_html += "<h4>* 상세 내용</h4>" + "<p>" + restaurant.restaurant_content + "</p><br>"
    #     mail_html += "<h4>* 관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
    #     mail_html += "<br>"
    # mail_html += "</body></html>"
    # # print(mail_html)

    # # smtp
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # server.login(id, pw)

    # # msg
    # msg = MIMEMultipart('alternative')
    # msg['Subject'] = inputTitle
    # msg['From'] = id
    # msg['To'] = inputReceiver
    # mail_html = MIMEText(mail_html, 'html')
    # msg.attach(mail_html)
    # # print(msg['To'], type(msg['To']))
    # server.sendmail(msg['From'], msg['To'].split(','), msg.as_string()) # 받는 사람 여럿일 때 split
    # server.quit()
    # return HttpResponseRedirect(reverse('index'))