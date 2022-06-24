from django.shortcuts import render
from .models import Student
from .threads import CreateStudentThread
# Create your views here.


def home(request):
    count = 1000
    CreateStudentThread(count).start()
    contaxt = {'result':'Your task is started'}
    return render(request, 'home.html', context=contaxt)