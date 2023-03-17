from django.shortcuts import render

# Create your views here.
def three(request):
    return render(request, 'one.html')
def four(request):
    return render(request, 'two.html')        