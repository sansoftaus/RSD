from django.shortcuts import render
from Remote_Software.Development.forms import DevelopmentForm
from django.http import HttpResponseRedirect

import os

def Remote_Software_Development(request):
    if request.method == 'POST':
        form = DevelopmentForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            return HttpResponseRedirect('/Submitted_Code')
    else:
        form = DevelopmentForm()            
    return render(request, 'Development_form.html', {'form': form})

def Submitted_code(request):
    file_location = os.getcwd() + "/Remote_Software/App/Code.py"
    file_object = open(file_location, "rb+")
    message = file_object.readlines()
    file_object.close()
    return render(request, 'submitted_code.html', {'message': message}) 