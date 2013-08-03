# Include the Dropbox SDK libraries
from dropbox import client, rest, session

APP_KEY = 'jgrn1vwmfcp0lpf'
APP_SECRET = 'reftv8sfas3bte5'
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

f = open('/home/santee/workspace/Remote_Software/App/Code.py', 'rb')

response = client.put_file('/Remote_Software.py', f)
print "uploaded:", response
