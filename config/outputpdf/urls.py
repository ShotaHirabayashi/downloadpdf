
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.top,name ="top"),
    path('pdf/',views.getpdf, name='pdf'),
    path('download/',views.pdf_download, name='download'),
]