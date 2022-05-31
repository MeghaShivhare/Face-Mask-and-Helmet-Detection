from django.shortcuts import render, HttpResponse
from django.http import StreamingHttpResponse
from VISOR.face import VideoCamera, MaskDetect
from VISOR.helmet import VideoCamera, HelmetDetection
from VISOR.models import Contact
from django.contrib import messages
from datetime import datetime
# Create your views here.


def index(request):
    context = {
        'variable1': "This is Face Mask Detection Website",
        'variable2': "You are in Home Page"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        message = request.POST.get('message','')
        print(name,email,phone,address,message)
        contact = Contact(name=name, email=email, phone=phone, address=address, message=message, date = datetime.today())
        contact.save()  
        messages.success(request, 'Message has been send Successfully!')
    return render(request, 'contact.html')


# Face-Mask Detection 

def face(request):
    return StreamingHttpResponse(gen(MaskDetect()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# HelmetDetection

def helmet(request):
    return StreamingHttpResponse(gen(HelmetDetection()),
					content_type='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def terms(request):
    return render(request, 'terms.html')
