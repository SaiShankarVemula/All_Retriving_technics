from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q 

# Create your views here.



## Data taking using views through cmd
def insert_topic(request):
    tn=input('enter the topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is created')

def insert_webpage(request):
    tn=input('enter the topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    na=input('enter name: ')
    un=input('enter URL: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=un)[0]
    WO.save()
    return HttpResponse('webpage is created')

def insert_webpage(request):
    tn=input('enter the topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    na=input('enter name: ')
    un=input('enter URL: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=un)[0]
    WO.save()
    dt=input('enter date: ')
    an=input('enter Author: ')
    AO=Accessrecord.objects.get_or_create(name=WO,date=dt,author=an)[0]
    AO.save()
    return HttpResponse('webpage is created')





## Displaying the DB tables in Frontend using htmlpages

def display_topics(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    # Retrieving methods
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(topic_name='Cricket')
    webpages=Webpage.objects.filter(name='Dhoni')
    webpages=Webpage.objects.all()[::-1]
    webpages=Webpage.objects.all()[2::]
    webpages=Webpage.objects.all()[0:10:2]
    webpages=Webpage.objects.exclude(topic_name='Cricket')
    webpages=Webpage.objects.all().order_by('topic_name')
    webpages=Webpage.objects.all().order_by('-topic_name')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.all().order_by(Length('name').desc())

    # Field Lookups
    webpages=Webpage.objects.filter(name__contains='on')
    webpages=Webpage.objects.filter(name__startswith='R')
    webpages=Webpage.objects.filter(name__endswith='t')
    webpages=Webpage.objects.filter(name__in=['Rahul','Dhoni'])
    webpages=Webpage.objects.filter(name__regex='V\w+')
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name='Rahul') | Q(url__startswith='https'))
    webpages=Webpage.objects.filter(Q(name='Rahul') | Q(url__endswith='in/'))
    webpages=Webpage.objects.filter(Q(name='Virat') & Q(url__startswith='https'))
    webpages=Webpage.objects.filter(Q(name='Rahul') & Q(url__startswith='https'))
    
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    # Field lookups
    access=Accessrecord.objects.all()
    access=Accessrecord.objects.filter(date='2013-06-26')
    # access=Accessrecord.objects.filter(date='2013-jun-26') this type of date fromat give error
    access=Accessrecord.objects.filter(date__lt='2013-06-26')
    access=Accessrecord.objects.filter(date__gt='2013-06-26')
    access=Accessrecord.objects.filter(date__gte='2013-06-26')
    access=Accessrecord.objects.filter(date__year__lte='2018')
    access=Accessrecord.objects.filter(date__day__lt='15')
    access=Accessrecord.objects.filter(date__month__gte='04')

    d={'access':access}
    return render(request,'display_accessrecord.html',d)

def all(request):
    topics=Topic.objects.all()
    webpages=Webpage.objects.all()
    access=Accessrecord.objects.all()
    d={'topics':topics,'webpages':webpages,'access':access}
    return render(request,'all.html',d)