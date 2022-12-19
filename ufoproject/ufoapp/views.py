from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, "index.html", {'result': obj,'result2':obj2})


# def about(request):
#     return HttpResponse("This is About Page")
# def contact(request):
#     return render(request,"contact.html")
# def details(request):
#     return HttpResponse("This is Details Page")
# def thanks(request):
#     return render(request,"thanks.html")
