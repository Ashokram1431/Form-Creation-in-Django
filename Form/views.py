from django.shortcuts import render
from Form.forms import StaffForm
# Create your views here.


def index(request):
    form=StaffForm()
    return render(request,'index.html',{'form':form})