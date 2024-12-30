from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("welcome to Eshikhon. ")
def login(request):
    return HttpResponse("welcome to login page.") 
