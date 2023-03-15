from django.shortcuts import render

# Create your views here.
def coco(request):
    return render(request,'coco.html')


def shettle(request):
    return render(request,'shettle.html')


