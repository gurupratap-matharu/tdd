from django.shortcuts import render


def home_page(request):
    render(request, 'lists/home.html')
