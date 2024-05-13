from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse ("<h1>Success</h1>")
    else:
        user_form=RegistrationForm()
    return render(request, 'registeration.html', {'user_form':user_form})