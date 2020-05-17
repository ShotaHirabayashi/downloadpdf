from django.shortcuts import render
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os

# Create your views here.


def top(request):
    return render(request,"index.html",{})




def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 55)
    p.drawString(100,700, "Hello, Javatpoint.")
    p.showPage()
    p.save()
    return response



def pdf_download(request):
    path = 'static/pdf/'
    f = open(path+"file.pdf", "r",encoding="ISO8859-1")
    response = HttpResponse(FileWrapper(f), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=resume.pdf'
    f.close()
    return response



