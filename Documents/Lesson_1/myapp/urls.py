
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('404/',views.eror, name='eror'),
    path('about/',views.about, name='about'),
    path('booking/',views.booking, name='booking'),
    path('contact/',views.contact, name='contact'),
    path('service/',views.service, name='service'),
    path('team/',views.team, name='team'),
    path('testimonial/',views.testimonial, name='testimonial'),

    
]

