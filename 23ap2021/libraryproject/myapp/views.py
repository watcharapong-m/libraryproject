from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from urllib import request
from bs4 import BeautifulSoup
import json

import mysql.connector
from django.db.models import Q 

# from .getdata import *
from .models import DataProject
import datetime
from django.db import connection
from django.http import HttpResponse
import urllib

import datetime

def index(request):
    url = urllib.request.urlopen("http://projectcs.sci.ubu.ac.th/WatcharapongNasaree/libraryproject")
    html = url.read().decode('utf8')
    html[:60]

    soup = BeautifulSoup(html, 'html.parser')
    list_data = []
    for title in soup.find_all("a", {"class": "str-truncated"}):
        data = title.find("span")
        dataclean = data.get_text()
        if dataclean != "README.md":
            list_data.append(dataclean)
    base_url = "http://projectcs.sci.ubu.ac.th/WatcharapongNasaree/libraryproject/raw/master/"
    success_list = []
    for i in list_data:
        semi_url = base_url+i
        soup = urllib.request.urlopen(semi_url).read().decode('utf8')
        data = json.loads(soup)
            
        data['Name'],
        data['StudentID'],
        data['ProjectName'],
        data['Advisor'],
        data['Type'],
        data['GraduationYear'],
        data['Abstract'],
        data['Keyword'],
        data['Technology'],
        data['Award'],
        data['LinkGit'],
        # print(data)
        Value = []
        for i in data.values():
            Value.append(i)
        # print(Value)

        x = []
        for i in range(1):
            x.append(Value)
        # print(len(x))

        for i in range(len(x)):
            StudentID = x[i][0]
            Name = x[i][1]
            ProjectName = x[i][2]
            Advisor = x[i][3]
            Type = x[i][4]
            GraduationYear = x[i][5]
            Abstract = x[i][6]
            Keyword = x[i][7]
            Technology = x[i][8]
            Award = x[i][9]
            LinkGit = x[i][10]
            
            DataProject.objects.update_or_create(StudentID=StudentID, Name=Name, ProjectName=ProjectName, Advisor=Advisor, Type=Type, GraduationYear=GraduationYear, Abstract=Abstract, Keyword=Keyword, Technology=Technology, Award=Award, LinkGit=LinkGit)
            
    return render(request, 'myapp/index.html')

def Fetchbytypeentertainment(request):
    entertainments = DataProject.objects.filter(Type='เพื่อความบันเทิง')
    return render(request,'myapp/entertainment.html', {'entertainments':entertainments})

def Fetchbytypelearning(request):
    learning = DataProject.objects.filter(Type='เพื่อส่งเสริมการเรียนรู้')
    return render(request,'myapp/learning.html', {'learning':learning})

def Fetchbytypedisabledandelderly(request):
    disabledandelderly = DataProject.objects.filter(Type='เพื่อช่วยคนพิการและผู้สูงอายุ')
    return render(request,'myapp/entertainment.html', {'disabledandelderly':disabledandelderly})

def Fetchbytypescienceadntecnology(request):
    scienceadntecnologys = DataProject.objects.filter(Type='การพัฒนาด้านวิทยาศาสตร์และเทคโนโลยี')
    return render(request,'myapp/scienceadntecnology.html', {'scienceadntecnologys':scienceadntecnologys})

def Fetchbytypemobileapplication(request):
    mobileapplications = DataProject.objects.filter(Type='Mobile Application โปรแกรมเพื่อการประยุกต์ใช้งานบนเครือข่ายสำหรับอุปกรณ์คอมพิวเตอร์เคลื่อนที่')
    # mobileapplications = DataProject.objects.raw('SELECT * FROM librarprojectapp_dataproject WHERE Type = Mobile Application โปรแกรมเพื่อการประยุกต์ใช้งานบนเครือข่ายสำหรับอุปกรณ์คอมพิวเตอร์เคลื่อนที่')
    # print('1111111111111')
    return render(request,'myapp/mobileapplications.html', {'mobileapplications':mobileapplications})

def year2563(request):
    years = DataProject.objects.filter(GraduationYear='2563')
    return render(request, 'myapp/2563.html', {'years':years})

def year2564(request):
    years = DataProject.objects.filter(GraduationYear='2564')
    return render(request, 'myapp/2564.html', {'years':years})

def year2565(request):
    years = DataProject.objects.filter(GraduationYear='2565')
    return render(request, 'myapp/2565.html', {'years':years})

def year2566(request):
    years = DataProject.objects.filter(GraduationYear='2566')
    return render(request, 'myapp/2566.html', {'years':years})

def year2567(request):
    years = DataProject.objects.filter(GraduationYear='2567')
    return render(request, 'myapp/2567.html', {'years':years})

def detail(request, id):
    # data0266 = DataProject.objects.all()
    datadetail = DataProject.objects.filter(id=id)
    # print(DataProject.objects.all())
    print('ID :', id)
    return render(request, 'myapp/detail.html',{'datadetail':datadetail})

# def datanew(request):
#     datanew = DataProject.objects.all()
#     print(datanew)
#     print('Success')
#     return render(request, 'myapp/index.html', {'datanew':datanew})

def dataAll(request):
    alldata = DataProject.objects.all()
    return render(request, 'myapp/all.html', {'alldata':alldata})

def latest(request):
    latest  = DataProject.objects.all()[:3]
    print(latest)
    return render(request, 'myapp/index.html', {'latest':latest})

def search(request):
    alldata = DataProject.objects.all()
    return render(request, 'myapp/search.html', {'alldata':alldata})