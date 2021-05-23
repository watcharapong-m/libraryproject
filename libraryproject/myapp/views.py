from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from urllib import request
from bs4 import BeautifulSoup
import json

import mysql.connector
from django.db.models import Q

from .models import DataProject
import datetime
from django.db import connection
from django.http import HttpResponse
import urllib

import datetime
from datetime import date

import datetime, pytz
tz = pytz.timezone('Asia/Bangkok')

def index(request):
    
    today = date.today()
    # timenow = today.strftime("%d/%m/%Y %H:%M:%S")

    # now1 = datetime.datetime.now(tz)
    # month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now1.month]
    # thai_year = now1.year + 543
    # time_str = now1.strftime('%H:%M:%S')
    # timenow = now1.day, month_name, thai_year, time_str
    # print(timenow)
    # print("%d %s %d %s"%(now1.day, month_name, thai_year, time_str))

    url = urllib.request.urlopen(
        "http://projectcs.sci.ubu.ac.th/WatcharapongNasaree/libraryproject")
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
    x = []
    for i in list_data:
        semi_url = base_url+i
        soup = urllib.request.urlopen(semi_url).read().decode('utf8')
        
        try:
            # data = json.loads(soup)
            data = json.loads(soup, strict=False)
        except:
            return render(request, 'myapp/index.html',{'years': getYear()})
        else:
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
            Value = []
            for i in data.values():
                Value.append(i)

            
            for i in range(1):
                x.append(Value)

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
            # print(x)
    AllStudentID = []
    datas = DataProject.objects.all()
    for std in datas :
        AllStudentID.append(std.StudentID)
    for i in range(len(x)):
        if x[i][0] in AllStudentID:
            pass
        else:
            StudentID = x[i][0]
            Name = x[i][1]
            ProjectName = x[i][2]
            Advisor = x[i][3]
            Type= x[i][4]
            GraduationYear = x[i][5]
            Abstract = x[i][6]
            Keyword = x[i][7]
            Technology = x[i][8]
            Award = x[i][9]
            LinkGit = x[i][10]
            DataProject.objects.update_or_create(StudentID=StudentID, Name=Name, ProjectName=ProjectName, Advisor=Advisor, Type=Type,GraduationYear=GraduationYear, Abstract=Abstract, Keyword=Keyword, Technology=Technology, Award=Award, LinkGit=LinkGit, created_at = today)
    return render(request, 'myapp/index.html',{'years': getYear()})

def getYear():
    datas = DataProject.objects.all()
    years = []
    for data in datas:
            data.GraduationYear
            if data.GraduationYear not in years:
                years.append(data.GraduationYear)
    return years

def Fetchbytypeentertainment(request):
    entertainments = DataProject.objects.filter(Type='โปรแกรมเพื่อความบันเทิง')
    return render(request, 'myapp/entertainment.html', {'entertainments': entertainments})


def Fetchbytypelearning(request):
    learning = DataProject.objects.filter(
        Type='โปรแกรมเพื่อส่งเสริมทักษะการเรียนรู้')
    return render(request, 'myapp/learning.html', {'learning': learning})


def Fetchbytypedisabledandelderly(request):
    disabledandelderly = DataProject.objects.filter(
        Type='เพื่อช่วยคนพิการและผู้สูงอายุ')
    return render(request, 'myapp/entertainment.html', {'disabledandelderly': disabledandelderly})


def Fetchbytypescienceadntecnology(request):
    scienceadntecnologys = DataProject.objects.filter(
        Type='การพัฒนาด้านวิทยาศาสตร์และเทคโนโลยี')
    return render(request, 'myapp/scienceadntecnology.html', {'scienceadntecnologys': scienceadntecnologys})


def Fetchbytypemobileapplication(request):
    mobileapplications = DataProject.objects.filter(
        Type='Mobile Application โปรแกรมเพื่อการประยุกต์ใช้งานบนเครือข่ายสำหรับอุปกรณ์คอมพิวเตอร์เคลื่อนที่')
    return render(request, 'myapp/mobileapplications.html', {'mobileapplications': mobileapplications})

def year(request, year):
    print('year: ',year)
    if year == 'all':
        alldata = DataProject.objects.all()
        return render(request, 'myapp/all.html', {'alldata': alldata})
    elif year == 'search':
        alldata = DataProject.objects.all()
        return render(request, 'myapp/search.html', {'alldata': alldata})
    years = DataProject.objects.filter(GraduationYear=year)
    return render(request, 'myapp/year.html', {'years': years,'numberyear':year})


def detail(request, id):
    datadetail = DataProject.objects.filter(id=id)
    month = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม", "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
    for i in datadetail.iterator():
        Link = i.LinkGit.split("http://")
        print(Link)
        if (len(Link)== 2):
            data = {
                "Name": i.Name,
                "StudentID" : i.StudentID,
                "ProjectName" : i.ProjectName,
                "Type" : i.Type,
                "GraduationYear" : i.GraduationYear,
                "Abstract" : i.Abstract,
                "Keyword" : i.Keyword,
                "Technology" : i.Technology,
                "Award" : i.Award,
                "LinkGit" : f'http://{Link[1]}',
                "datetime" : f'วันที่ {i.created_at.strftime("%d")} เดือน {month[int(i.created_at.strftime("%m"))-1]} พ.ศ. {int(i.created_at.strftime("%Y"))+543}'
            }
        else: 
            data = {
                "Name": i.Name,
                "StudentID" : i.StudentID,
                "ProjectName" : i.ProjectName,
                "Type" : i.Type,
                "GraduationYear" : i.GraduationYear,
                "Abstract" : i.Abstract,
                "Keyword" : i.Keyword,
                "Technology" : i.Technology,
                "Award" : i.Award,
                "LinkGit" : f'http://{Link[0]}',
                "datetime" : f'วันที่ {i.created_at.strftime("%d")} เดือน {month[int(i.created_at.strftime("%m"))-1]} พ.ศ. {int(i.created_at.strftime("%Y"))+543}'
            }
    return render(request, 'myapp/detail.html', {'datadetail': data})


def dataAll(request):
    alldata = DataProject.objects.all()
    return render(request, 'myapp/allcatefory.html', {'alldata': alldata})


def latest(request):
    latest = DataProject.objects.all()[:3]
    print(latest)
    return render(request, 'myapp/index.html', {'latest': latest})


def search(request):
    alldata = DataProject.objects.all()
    return render(request, 'myapp/search.html', {'alldata': alldata})