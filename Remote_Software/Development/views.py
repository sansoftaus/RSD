from django.shortcuts import render
from Remote_Software.Development.forms import DevelopmentForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Include the Dropbox SDK libraries
from dropbox import client, rest, session

import subprocess
import os

#Global variable from forms.py
from Remote_Software.Development.forms import Global

#DropBox Integration
    
#APP_KEY = 'ar6snxa76ndx5iz'
#APP_SECRET = 'cq1wjz72vdou2bq'

APP_KEY = 'jgrn1vwmfcp0lpf'
APP_SECRET = 'reftv8sfas3bte5'
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
    return render(request, 'Development_form.html', {'form': form})

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
    
    file_location = os.getcwd() + "/Remote_Software/App/" + Global.app_name + ".py"
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
    
    dropbox_sess.obtain_access_token(dropbox_request_token)
    dropbox_client = client.DropboxClient(dropbox_sess)
    Account_info = dropbox_client.account_info()
    
    #Delete if there is any previously created tar files
    command0 = 'rm -rf ' + os.getcwd() + '/Remote_Software/App/' + Global.app_name +'.tar'
    os.system(command0)
    
    CWD = os.getcwd()
    os.chdir(CWD+'/Remote_Software/App/pyinstaller-2.0')    
    
    #Converting the given user code (.py) to an executable using pyinstaller library
    command1 = 'python '+ CWD + '/Remote_Software/App/pyinstaller-2.0/pyinstaller.py -D ' + CWD + '/Remote_Software/App/' + Global.app_name + '.py'
    os.system(command1)
    
    #The executable directory is compressed through tar 
    command2 = 'tar -cvf ' + CWD + '/Remote_Software/App/' + Global.app_name + '.tar ' + CWD + '/Remote_Software/App/pyinstaller-2.0/' + Global.app_name +'/dist/' + Global.app_name
    os.system(command2)
    
    #The generated Code (folder) inside pyinstaller-2.0 is deleted after creating into App_name.tar
    command3 = 'rm -rf /home/santee/workspace/Remote_Software/App/pyinstaller-2.0/' + Global.app_name
    os.system(command3)    
    
    os.chdir(CWD)
    
    f = open('/home/santee/workspace/Remote_Software/App/' + Global.app_name + '.py', 'rb')
    response = dropbox_client.put_file('/' + Global.app_name + '.py', f, overwrite=True )
    f.close()    
        
    f = open('/home/santee/workspace/Remote_Software/App/' + Global.app_name + '.tar', 'rb')    
    response = dropbox_client.put_file('/' + Global.app_name + '.tar', f, overwrite=True)
    f.close()
    
    #Clean up commands
    command4 = 'rm -rf /home/santee/workspace/Remote_Software/App/*.py /home/santee/workspace/Remote_Software/App/*.tar'
    os.system(command4)    
    
    
    #Converting the dictionary into Lists
    response_keys = response.keys()
    response_values = response.values()
    account_keys = Account_info.keys()
    account_values = Account_info.values()

    #Empty List to store the responses
    response_list = []

    #First add the account information into the empty list
    for i in xrange(len(account_keys)):
        response_list.append(str(account_keys[i]) + " : " + str(account_values[i]))

    #Second add the response information into the empty list
    for i in xrange(len(response_keys)):
        response_list.append(str(response_keys[i]) + " : " + str(response_values[i]))

    return render(request, 'Thank_You.html', {'response': response_list})
                        