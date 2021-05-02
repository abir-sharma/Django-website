from django.shortcuts import render,HttpResponse
from django.contrib import messages
from Home.models import Contact
from datetime import datetime
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def pubg(request):
    return render(request,'pubg.html')

def valorant(request):
    return render(request,'valorant.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent!')
    return render(request,'contact.html')


