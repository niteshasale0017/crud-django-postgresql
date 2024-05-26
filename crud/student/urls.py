from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.add_show,name="addshow"),
    path('delete/<int:id>/',views.delete,name="deletedata"),
    path('update/<int:id>',views.update,name="updatedate")
    
]