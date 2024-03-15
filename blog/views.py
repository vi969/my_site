from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main_page(request):
    return HttpResponse('<h2>Main page</h2>')
