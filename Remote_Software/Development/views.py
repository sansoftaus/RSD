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
    #try:
        Code_Errors = "Code was successfully executed without any Errors!"
        Code_Output = ""
        Execute = None
        file_location = os.getcwd() + "/Remote_Software/App/Code.py"
        file_object = open(file_location, "rb+")
        message = "".join(file_object.readlines())    
        file_object.close()
        cmd = "python " + file_location
        #Execute = subprocess.Popen(cmd, stdout=subprocess.STDOUT, stderr = subprocess.PIPE)
        #Code_Output = Execute.stdout.read() 
    #except subprocess.CalledProcessError:
        #Code_Errors = Execute.stderr.read()
        return render(request, 'submitted_code.html', {'message': message, 'output':"Code_Output", 'errors':Code_Errors})