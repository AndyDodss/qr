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
    return HttpResponse(link)
    #return redirect(str(link))


