from django.urls import path
from.import views

urlpatterns=[
   path('',views.homepageview,name="home"),
   path('about',views.aboutpageview,name="About us page"),
   path('contact',views.contactpageview,name="Contact us page"),
   path('form',views.myform,name="Myform"),
   path('formprocess',views.process,name="Process"),
 
]