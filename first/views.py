from django.shortcuts import render

# Create your views here.
def main(request) :
    return render(request, 'first/main.html')

def one(request) :
    return render(request, 'first/one.html')

def two(request) :
    return render(request, 'first/two.html')

def one_1(request) :
    return render(request, 'first/one_1.html')

def one_2(request) :
    return render(request, 'first/one_2.html')

def one_3(request) :
    return render(request, 'first/one_3.html')

def two_1(request) :
    return render(request, 'first/two_1.html')

def two_2(request) :
    return render(request, 'first/two_2.html')

def two_3(request) :
    return render(request, 'first/two_3.html')