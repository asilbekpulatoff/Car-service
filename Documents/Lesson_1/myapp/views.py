

from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def booking(request):
    return render(request, 'blog/booking.html')

def contact(request):
    return render(request, 'blog/contact.html')

def service(request):
    return render(request, 'blog/service.html')

def team(request):
    return render(request, 'blog/team.html')

def testimonial(request):
    return render(request, 'blog/testimonial.html')

def eror(request):
    return render(request, 'blog/404.html')

