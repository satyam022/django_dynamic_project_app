from django.shortcuts import render
from myapp.models import contactEnquiry


# Create your views here.

def index(request):
    return render(request, 'index.html')


def Hacking(request):


    return render(request, 'hacker.html')


def indexPage(request):
    return render(request, 'index-2.html')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def blogsingle(request):
    return render(request, 'blog-single.html')


def contact(request):
    return render(request, 'contact.html')


def saveEnquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        en = contactEnquiry(name=name, email=email, phone=phone, subject=subject, message=message)
        en.save()

    return render(request, 'contact.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def portfolio_details(request):
    return render(request, 'portfolio-details.html')


def service(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')
