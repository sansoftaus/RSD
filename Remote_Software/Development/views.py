from django.shortcuts import render
from Remote_Software.Development.forms import DevelopmentForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Include the Dropbox SDK libraries
from dropbox import client, rest, session

import subprocess
import os

#DropBox Integration
    
APP_KEY = 'ar6snxa76ndx5iz'
APP_SECRET = 'cq1wjz72vdou2bq'
ACCESS_TYPE = 'app_folder'

dropbox_sess = None
dropbox_request_token = None
dropbox_url = None

def Remote_Software_Development(request):   
    if request.method == 'POST':
        form = DevelopmentForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            return HttpResponseRedirect('/Submitted_Code')
    else:
        form = DevelopmentForm()            
    return render(request, 'Development_form.html', {'form': form, 'dropbox': "I dono"})

def Submitted_code(request):
    global dropbox_sess
    global dropbox_request_token
    global dropbox_url 
    
    dropbox_sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)    
    dropbox_request_token = dropbox_sess.obtain_request_token()
    # Make the user sign in and authorize this token
    dropbox_url = dropbox_sess.build_authorize_url(dropbox_request_token)    
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
    return render(request, 'submitted_code.html', {'message': message, 'output':Code_Output, 
                'errors':Code_Errors, 'dropbox_url':dropbox_url})

def Add_to_dropbox(request):
    global dropbox_sess
    global dropbox_request_token
    
    access_token = dropbox_sess.obtain_access_token(dropbox_request_token)
    dropbox_client = client.DropboxClient(dropbox_sess)
    
    f = open('/home/santee/workspace/Remote_Software/App/Code.py', 'rb')    
    response = dropbox_client.put_file('/Remote_Software.py', f)
    f.close()
    
    return HttpResponse("Your App is successfully uploaded into your DropBox location")
                        