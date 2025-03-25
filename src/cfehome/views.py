from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit

# Définir le chemin du fichier
this_dire = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs= PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "MyPage"
    html_template = "home.html"
    my_context={
        "page_title": my_title,
        "page_visit_count":page_qs.count(),
        "total_visit_count": qs.count(),
         "percent": (page_qs.count()/qs.count())*100
    }
    path= request.path
    print("path",path)
    
    PageVisit.objects.create()
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)
    

def my_old_home_page_view(request, *args, **kwargs):
    my_title = "MyPage"
    my_context={
        "page_title": my_title
    }
    html_="""
    <!DOCTYPE html>
    <html> 
    <body>
    <h1>{page_title}Hello World</h1> 
    </body> 
    </html> 
    """.format(**my_context)
    return HttpResponse(html_)
    

