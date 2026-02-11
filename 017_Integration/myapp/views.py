from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMessage
from django.conf import settings


# Create your views here.
def index(request):
    return render(request,"index.html")

def sendmail(request):   
    try :
        subject = request.POST['subject']
        message = request.POST['message']
        from_email = settings.EMAIL_HOST_USER
        recipient_list  = [request.POST['from']]

        send_mail(subject,message,from_email,recipient_list,html_message="<h1>Hello</h1>")
        return render(request,"index.html",{"msg":"Mail sent"})
    except Exception as e:
         return render(request,"index.html",{"msg":"something went wrong"})
    

def sendfile(request):
     msg =  EmailMessage("Test","testing",settings.EMAIL_HOST_USER,['chintan.tops@gmail.com'])
     msg.attach_file("media/avatar-1.jpg")
     msg.send()

     return HttpResponse("file sent")
   