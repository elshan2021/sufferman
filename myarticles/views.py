from django.shortcuts import render
from . import models

def articleslists(request):
    arts = models.Articles_db.objects.all().order_by('date')

    args =  {'mart' : arts}
    return render(request , 'myarticles/articleslist.html', args)
