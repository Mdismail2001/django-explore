from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return render(request, 'about.html')


def home(request):
    # data={
    #     'title':'National flag ',
    #     'heading':'Flag',
    #     'clist':['php','java','Django'],
    #     'number':[10,20,30,40,50],
 
    #     'student_details':[
    #         {'name':'ismail','phone': 18720855773},
    #         {'name':'sharif','phone': 40395029998}
    #     ]
    # }
    # return render(request, "index.html",data)
    return render(request, "home.html")



def contact(request):
    return render(request, "contact.html")

def namedetails(requst,nameid):
    return HttpResponse(nameid)