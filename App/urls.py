from django.urls import path
from App import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact', views.contactMe, name="contactMe"),
    path('insert', views.insertData, name="insertData")
]