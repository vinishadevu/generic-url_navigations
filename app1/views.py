from django.shortcuts import render

# Create your views here.
def cricket(request):
    return render(request,'cricket.html')


def kabaddi(request):
    return render(request,'kabaddi.html')








