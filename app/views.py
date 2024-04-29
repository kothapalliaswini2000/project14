from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    tn=input('enter topic_name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic is created successfully')