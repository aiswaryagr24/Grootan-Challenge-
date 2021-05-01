from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from .models import it as form 
def home(request):
    return render (request,'grootan.html')
class upload (View):
    def post(self,request):
       n=form()
       n.fil=request.FILES.get('fil')
       n.save()
       return render (request,'grootan.html')