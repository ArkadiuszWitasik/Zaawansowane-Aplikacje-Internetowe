from django.shortcuts import render
from django.http import HttpResponse

def all(request):
  return HttpResponse("<h1>Tu będą wyświetlane informacje o albumach z dany zdanych</h1>")

def details(request):
  return HttpResponse("<h1>Tu będą wyświetlane informacje na temat wybranego albumu</h1>")