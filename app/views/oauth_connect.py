import random, string
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask import session as login_session

from flask import make_response
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import requests
import json

from app.userConstruct import create_user
