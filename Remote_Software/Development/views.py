from django.shortcuts import render
from Remote_Software.Development.forms import DevelopmentForm
from django.http import HttpResponseRedirect

import subprocess
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
    Code_Errors = "App was successfully executed without any Errors!"
    Code_Output = "App failed to Execute!"
    Execute = None
    file_location = os.getcwd() + "/Remote_Software/App/Code.py"
    file_object = open(file_location, "rb+")
    message = "".join(file_object.readlines())    
    file_object.close()
    Execute = subprocess.Popen(['python', file_location], stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    Executed_results = Execute.communicate()
    if Execute.returncode == 0:
        Code_Output = "".join(Executed_results)
    else:
        Code_Errors = "".join(Executed_results)
    return render(request, 'submitted_code.html', {'message': message, 'output':Code_Output, 'errors':Code_Errors})