from django.shortcuts import render


def index(request):
    template = 'html/index.html'
    return render(request, template)