# ItemCataloger

## Project specifications:

* Implemented Google's OAuth authentication for users
* Local permission systems implented for 'CRUD' operations
* 'CRUD' operations for user to store items and their respective description in relevant categories 
* CRSF protection is implemented for 'CRUD' operations
* JSON API endpoints are provided

### Built with:

* Python 3.6
* SQLalchemy
* WTForms
* Flask
* Bootstrap

#### Requirements

This web application was built using a Vagrant virtual box and runs with Python 3.6 using Flask Microframework.
Key packages include WTForms to validate user's input and SQLalchemy to operate on a SQLite database.

#### Configurations

There are 2 files that need to be configured before start.
1) The 'config.py' file is located in the repo root directory. Adding an 'APP_SECRET_KEY' and a 'CSRF_SECRET_KEY' is recommeneded

2) A 'client_secrets.json' file is required. This should be saved in the repo root directory. This will need to include
Google's OAuth API information. Refer to Google's documentaion:

[Using OAuth 2.0 to Access Google APIs - Google Developers](https://developers.google.com/identity/protocols/OAuth2)

Add in your own "client_id" and "client_secret". The file should look similar to:

```
{
    "web": {
        "client_id": "ADD_CLIENT_ID",
        "project_id": "item-catalog-188904",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "ADD_SECRET",
        "redirect_uris": ["http://localhost:8000/login","http://localhost:8000/gconnect"]
        "javascript_origins": ["http://localhost:8000"]
    }
}
```

#### Vagrant

Next, fire up Vagrant.

Move to the project folder e.g.:
```
$ cd /vagrant/fsnd-item_catalog
```

Fire up Vagrant:
```
# load vagrant
$ vagrant up

# login via ssh
$ vagrant ssh
```

Once Vagrant is up:
```
# cd to the vagrant shared folder:
$ cd /vagrant

# then move to the project folder:
$ cd fsnd-item_catalog

# alternatively, just do this
$ cd /vagrant/fsnd-item_catalog
```

For later on, to exit/stop Vagrant:
```
# to exit the virtual box:
$ exit

# to stop Vagrant and not lose any data
$ vagrant halt
```

#### Run the webserver

Ensure you are back in the root directory and then enter the command `webserver.py`. The app server will launch. 
Navigate to `localhost:8000` in your browser to see the app.

