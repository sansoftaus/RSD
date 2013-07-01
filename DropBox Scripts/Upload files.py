# Include the Dropbox SDK libraries
from dropbox import client, rest, session

APP_KEY = 'ar6snxa76ndx5iz'
APP_SECRET = 'cq1wjz72vdou2bq'
ACCESS_TYPE = 'app_folder'

sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

request_token = sess.obtain_request_token()

# Make the user sign in and authorize this token
url = sess.build_authorize_url(request_token)
print "url:", url
print "Please authorize in the browser. After you're done, press enter."
raw_input()

# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)

client = client.DropboxClient(sess)
print "linked account:", client.account_info()

f = open('E:/Final MEng Project/1208175212040673_Santhosh.exe', 'rb')

response = client.put_file('/Cpp_Project_2.exe', f)
print "uploaded:", response
