from django.db import models

# Create your models here.
class DataProject(models.Model):
    Name = models.CharField(max_length=50, blank=False)
    StudentID = models.CharField(max_length=11, blank=False)
    ProjectName = models.CharField(max_length=255,blank=False)
    Advisor = models.CharField(max_length=50,blank=False)
    Type = models.CharField(max_length=255, blank=False)
    GraduationYear = models.CharField(max_length=4, blank=False)
    Abstract = models.TextField( blank=False)
    Keyword = models.CharField(max_length=255, blank=False)
    Technology = models.CharField(max_length=255, blank=False)
    Award = models.CharField(max_length=255, blank=False)
    LinkGit = models.CharField(max_length=100, blank=False)
    # TimeAdd = models.DateTimeField(blank=False)