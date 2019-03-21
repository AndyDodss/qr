from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import login,authenticate
import cv2
from pyzbar import pyzbar
# Create your views here.
from .video import func

def index(request):

    return render(request,'index.html')


def scann(request):
    link = func()
    return redirect(str(link))
    #return redirect(str(link))
def qr2(request):
    place=request.GET.get('place')
    branch=request.GET.get('branch')
    server=request.GET.get('server')
    return HttpResponse(str(place)+str(branch)+str(server))
    


