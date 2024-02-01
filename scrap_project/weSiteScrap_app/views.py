from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from django.shortcuts import render
import requests

from weSiteScrap_app.models import Links

# Create your views here.

def indexViews(request):
    if request.method == 'POST':
        link_new = request.POST.get('page','')
        urls = requests.get(link_new)
        beautysup = BeautifulSoup(urls.text,'html.parser')

        for link in beautysup.find_all('a'):
            li_address = link.get('href')
            li_name = link.string
            Links.objects.create(address=li_address, stringName=li_name)
        return HttpResponseRedirect('/')
    else :
        data_val = Links.objects.all()

    return render(request, 'home.html',{'data_val':data_val})