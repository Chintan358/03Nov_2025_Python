from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
import requests
import razorpay

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

def sendsms(request):
    
    phone = request.POST['phone']
    message = request.POST['message']
    APIKEY=""
    url = f"https://www.fast2sms.com/dev/bulkV2?authorization={APIKEY}&route=q&message={message}&numbers={phone}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)
    return render(request,"index.html",{"success":"message sent successfully"})
   


def payment(request):

    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_SF5R7ur5nvvYLR", "NgUDBnx9JpMGHTWixBznB0S3"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
   
    return JsonResponse(payment)