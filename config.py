import json

# instance/config.py
GOOGLE_CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Cataloguer"
APP_SECRET_KEY = 'super_secret_key'
CSRF_SECRET_KEY = b'crsf_secret'
app_debug = True
app_run_host = '0.0.0.0'
app_run_port = port = 8000
