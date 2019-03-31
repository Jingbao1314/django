from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    context['condition1'] = '1610'
    context['condition2'] = '7721'
    return render(request, 'hello.html', context)


def index(request):
    context = {}
    context['first_name'] = 'xxxx'
    context['first_company'] = 'XXXX'
    return render(request, 'index.html', context)
@csrf_exempt
def page_not_found(request):
 return render_to_response('404.html')

@csrf_exempt
def page_error(request):
 return render_to_response('500.html')