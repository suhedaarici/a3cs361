from django.shortcuts import render
def mysearch (request):
    if request.method == "GET":
        return render(request, 'webapp.html', {})


from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from forms import Teacher

def index(request):
    if request.method=="GET":
        teacher= Teacher
        return render_to_response("webapp.html",{"types":teacher})
    #return HttpResponse("Hello, world. You're at the polls index.")


def search(request):
    if 'q' in request.GET:
        message = 'You searched for : %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

