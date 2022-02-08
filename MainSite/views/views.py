from django.shortcuts import redirect ,render
from django.views import View
def index(request):
    # create a HttpResponse object and return it.
    return render(request, 'home.html')
def login(request):
    return  render(request, 'Login.html')