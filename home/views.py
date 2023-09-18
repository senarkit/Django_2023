from django.shortcuts import render, HttpResponse

# Create your views here.
def home(requests):
    return render(requests, 'home.html')

def SGN(requests):
    return render(requests, 'SGN.html')

def HASE(requests):
    return render(requests, 'HASE.html')

def MSB(requests):
    # return HttpResponse("This is page for M&S Market")
    return render(requests, "MSB.html")