from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

# Définir le chemin du fichier
this_dire = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
   return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs= PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent= (page_qs.count()/qs.count())*100
    except:
        percent=0
    my_title = "MyPage"
    html_template = "home.html"
    my_context={
        "page_title": my_title,
        "page_visit_count":page_qs.count(),
        "total_visit_count": qs.count(),
         "percent": percent
    }
    path= request.path
    print("path",path)
    
    PageVisit.objects.create()
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
    