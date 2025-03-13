from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def landing_page(request):
    return HttpResponse("Hello world of pollssss")