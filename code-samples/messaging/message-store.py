#!/usr/bin/env python
from ringcentral import SDK
import os,sys
from dotenv import load_dotenv
load_dotenv()

CLIENTID     = os.environ.get('RC_CLIENT_ID')
CLIENTSECRET = os.environ.get('RC_CLIENT_SECRET')
SERVER       = os.environ.get('RC_SERVER_URL')
USERNAME     = os.environ.get('RC_USERNAME')
PASSWORD     = os.environ.get('RC_PASSWORD')
EXTENSION    = os.environ.get('RC_EXTENSION')

rcsdk = SDK( CLIENTID, CLIENTSECRET, SERVER )
platform = rcsdk.platform()
try:
  platform.login(USERNAME, EXTENSION, PASSWORD)
except:
  sys.exit("Unable to authenticate to platform. Check credentials.")

try:
    response = platform.get('/restapi/v1.0/account/~/extension/~/message-store',
	                    {
	                        'messageType': ['SMS']
	                    })
except Exception as e:
    sys.exit( e )
else:   
    print( response.text() )
    sys.exit(0)
